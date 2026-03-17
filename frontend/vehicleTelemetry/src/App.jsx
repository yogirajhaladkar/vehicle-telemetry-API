import { createBrowserRouter, createRoutesFromElements, Route, RouterProvider } from 'react-router-dom'
import Layout from './Layout/Layout'
import './App.css'

const rtr = createBrowserRouter(
  createRoutesFromElements(
    <Route path="/" element={<Layout />}>
    </Route>
  )
)

function App() {

  return (
    <>
      <RouterProvider router={rtr} />
    </>
  )
}

export default App
