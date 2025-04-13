import React from "react";
import { useNavigate } from "react-router-dom";

export default (props: { id: number, title: string, content: string, publisher: string}): React.ReactElement => {
  const navigate = useNavigate();
  
  const styles = {
    border: '2px solid black',
  }

  const deletePost = async () => {
    const result = await fetch('http://127.0.0.1:8000/post', {
      method: 'DELETE',
      headers: {
        'Content-Type': 'application/json',
        'Authorization': `Bearer ${sessionStorage.getItem('token')}`
      },
      body: JSON.stringify({ post_id: props.id })
    });

    const json = await result.json();
    
    if (result.status !== 200) {
      window.alert(json.detail);
      
      if (result.status === 401) {
        navigate('/');
      }

      return;
    }

    window.alert('Post deleted successfully');
    navigate(0);
  }

  const updatePost = () => {
    navigate('/update', { state: { id: props.id, title: props.title, content: props.content }})
  }
  
  return (
    <div style={styles}>
      <h3>Title: {props.title}</h3>
      <p><b>Content:</b><br/>{props.content}</p>
      <p><b>Publisher:</b> {props.publisher}</p>
      <div>
      <button onClick={deletePost}>Delete</button>
      <button onClick={updatePost}>Update</button>
      </div>
    </div>
  );
}
