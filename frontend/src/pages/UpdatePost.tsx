import React, { FormEvent, useState } from "react";
import { useLocation, useNavigate } from "react-router-dom";

export default (): React.ReactElement => {
  const location = useLocation();
  const { id, title, content } = location.state;  
  const [postTitle, setPostTitle] = useState(title);
  const [postContent, setPostContent] = useState(content);
  const navigate = useNavigate()

  
  const handleSubmit = async (e: FormEvent) => {
    e.preventDefault();
    
    const result = await fetch('http://127.0.0.1:8000/post', {
      method: 'PUT',
      headers: {
        'Content-Type': 'application/json',
        'Authorization': `Bearer ${sessionStorage.getItem('token')}`
      },
      body: JSON.stringify({ post_id: id, title: postTitle, content: postContent })
    });

    const json = await result.json();

    if (result.status !== 200) {
      window.alert(json.detail);
      
      if (result.status === 401) {
        navigate('/');
      }

      return;
    }

    window.alert('Post updated successfully');
    navigate('/feed');
  }
  
  return (
    <div>
      <h2>Update Post</h2>
      <form onSubmit={handleSubmit}>
        <label htmlFor='title'>Title</label>
      <input type='text' id='title' value={postTitle} onChange={(e) => setPostTitle(e.target.value)}/>

        <br/>
      
        <label htmlFor='content'>Content</label>
      <input type='text' id='content' value={postContent} onChange={(e) => setPostContent(e.target.value)}/>

        <br/>
        <input type='submit'/>
      </form>
    </div>
  );
}
