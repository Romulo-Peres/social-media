import React, { FormEvent, useState } from "react";
import { useNavigate } from "react-router-dom";

export default (): React.ReactElement => {
  const [title, setTitle] = useState('');
  const [content, setContent] = useState('');
  const navigate = useNavigate()
  
  const handleSubmit = async (e: FormEvent) => {
    e.preventDefault();
    
    const result = await fetch('http://127.0.0.1:8000/post', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'Authorization': `Bearer ${sessionStorage.getItem('token')}`
      },
      body: JSON.stringify({ title, content })
    });

    const json = await result.json();

    if (result.status !== 201) {
      window.alert(json.detail);
      
      if (result.status === 401) {
        navigate('/');
      }

      return;
    }

    window.alert('Post created successfully');
    navigate('/feed');
  }
  
  return (
    <div>
      <h2>New Post</h2>
      <form onSubmit={handleSubmit}>
        <label htmlFor='title'>Title</label>
        <input type='text' id='title' onChange={(e) => setTitle(e.target.value)}/>

        <br/>
      
        <label htmlFor='content'>Content</label>
        <input type='text' id='content' onChange={(e) => setContent(e.target.value)}/>

        <br/>
        <input type='submit'/>
      </form>
    </div>
  );
}
