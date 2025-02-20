import React from 'react'
import ReactDOM from 'react-dom/client'

import './stylesheets/root.css'
import './stylesheets/auth.css'
import './stylesheets/topbar.css'
import './stylesheets/app.css'
import './stylesheets/watch.css'
import './stylesheets/search.css'

import Root from './routes/root.jsx'
import Auth from './routes/auth.jsx'
import App from './routes/app.jsx'
import Watch from './routes/watch.jsx'
import Search from './routes/search.jsx'
import ErrorPage from './routes/error.jsx'

import {
  createBrowserRouter,
  RouterProvider,
} from "react-router-dom";

const router = createBrowserRouter([
  {
    path: "/",
    element: <Root/> ,
    errorElement: <ErrorPage/>,
    children: [
      // {
      //   index: true,
      //   element: <Index/>
      // },
      // {
      //   path: "/projects",
      //   element: <Projects/>
      // },
    ]
  },
  {
    path: "/app",
    element: <App/> ,
    errorElement: <ErrorPage/>,
  },
])

ReactDOM.createRoot(document.getElementById('root')).render(
  <React.StrictMode>
     <RouterProvider router={router}/>
  </React.StrictMode>,
)
