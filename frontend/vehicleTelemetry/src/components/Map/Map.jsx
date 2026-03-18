import { useEffect, useRef, useState } from "react";
import { useSelector } from "react-redux";

let googleMapsPromise = null;

function loadGoogleMaps(apiKey) {
    if (window.google?.maps) {
        return Promise.resolve(window.google);
    }

    if (googleMapsPromise) {
        return googleMapsPromise;
    }

    googleMapsPromise = new Promise((resolve, reject) => {
        const script = document.createElement("script");
        script.src = `https://maps.googleapis.com/maps/api/js?key=${apiKey}`;
        script.async = true;
        script.defer = true;
        script.dataset.googleMaps = "true";
        script.onload = () => resolve(window.google);
        script.onerror = () => reject(new Error("Failed to load Google Maps"));
        document.head.appendChild(script);
    });

    return googleMapsPromise;
}

export default function Map() {
    const dynamicData = useSelector((state) => state.vehicle.dynamicData);
    const apiKey = import.meta.env.VITE_GOOGLE_MAPS_API_KEY;
    const mapContainerRef = useRef(null);
    const mapRef = useRef(null);
    const markerRef = useRef(null);
    const [mapError, setMapError] = useState("");

    const latitude = Number(dynamicData?.latitude);
    const longitude = Number(dynamicData?.longitude);
    const hasValidCoordinates = Number.isFinite(latitude) && Number.isFinite(longitude);

    useEffect(() => {
        if (!apiKey || !hasValidCoordinates || !mapContainerRef.current) {
            return;
        }

        let isCancelled = false;

        loadGoogleMaps(apiKey)
            .then((google) => {
                if (isCancelled) {
                    return;
                }

                const position = { lat: latitude, lng: longitude };

                if (!mapRef.current) {
                    mapRef.current = new google.maps.Map(mapContainerRef.current, {
                        center: position,
                        zoom: 15,
                        mapTypeControl: false,
                        streetViewControl: false,
                    });

                    markerRef.current = new google.maps.Marker({
                        position,
                        map: mapRef.current,
                        title: dynamicData?.vehicleId || "Vehicle",
                    });
                } else {
                    mapRef.current.setCenter(position);
                    if (markerRef.current) {
                        markerRef.current.setPosition(position);
                    }
                }

                setMapError("");
            })
            .catch((error) => {
                if (!isCancelled) {
                    setMapError(error.message || "Unable to render map");
                }
            });

        return () => {
            isCancelled = true;
        };
    }, [apiKey, hasValidCoordinates, latitude, longitude, dynamicData?.vehicleId]);

    if (!dynamicData) {
        return <div className="h-full w-full grid place-items-center">No telemetry selected</div>;
    }

    if (!apiKey) {
        return (
            <div className="h-full w-full grid place-items-center px-4 text-center">
                Add VITE_GOOGLE_MAPS_API_KEY in your frontend .env file
            </div>
        );
    }

    if (!hasValidCoordinates) {
        return <div className="h-full w-full grid place-items-center">Latitude/Longitude not available</div>;
    }

    if (mapError) {
        return <div className="h-full w-full grid place-items-center">{mapError}</div>;
    }

    return (
        <div className="h-full w-full p-2">
            <div ref={mapContainerRef} className="h-full w-full rounded" />
        </div>
    );
}