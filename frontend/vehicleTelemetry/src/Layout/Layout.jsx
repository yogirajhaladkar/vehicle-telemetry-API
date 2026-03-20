import Header from '../components/Header/Header'
import Filter from '../components/Fillter/Filter'
import StaticData from '../components/Static/StaticData'
import DynamicData from '../components/Dynamic/DyanamicData'
import Map from '../components/Map/Map'

function Layout() {
    return (
        <div className='grid h-[100vh]
         grid-cols-[50%_50%] 
          grid-rows-[80px_80px_1fr_1fr]'
        >
            <div className='border row-start-1 col-span-2'>
                <Header />
            </div>
            <div className='border row-start-2 col-span-2'>
                <Filter />
            </div>
            <div className='border row-start-3 col-span-1 overflow-y-auto min-h-0'>
                <StaticData />
            </div>
            <div className='border row-start-4 col-span-1 overflow-y-auto min-h-0'>
                <DynamicData />
            </div>
            <div className='border row-start-3 row-end-5 col-span-2 min-h-0'>
                <Map />
            </div>
        </div>
    )
}

export default Layout