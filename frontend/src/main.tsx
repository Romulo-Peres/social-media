import { createRoot } from 'react-dom/client'
import { BrowserRouter, Route, Routes } from 'react-router-dom'
import Login from './pages/Login.tsx'
import Feed from './pages/Feed.tsx'
import CreatePost from './pages/CreatePost.tsx'
import UpdatePost from './pages/UpdatePost.tsx'

createRoot(document.getElementById('root')!).render(
  <BrowserRouter>
    <Routes>
    <Route path="/" element={<Login />}/>
    <Route path="/feed" element={<Feed />}/>
    <Route path="/create" element={<CreatePost />}/>
    <Route path="/update" element={<UpdatePost />}/>
    </Routes>
  </BrowserRouter>
)
