import { useEffect, useState } from "react";
import Post from "../components/Post";
import { Link, useNavigate } from "react-router-dom";

export default (): React.ReactElement => {
  const [posts, setPosts] = useState([]);
  const navigate = useNavigate();

  useEffect(() => {
    (async () => {
      console.log(sessionStorage.getItem('token'))
      const result = await fetch('http://127.0.0.1:8000/posts', {
        headers: {
          'Authorization': `Bearer ${sessionStorage.getItem('token')}`
        },
        method: 'GET'
      });

      const json = await result.json();

      if (result.status !== 200) {
        window.alert(json.detail);
        
        if (result.status === 401) {
          navigate('/');
        }
        
        return;
      }

      console.log(json);
      setPosts(json.posts);
    })();
  }, []);
  
  return (
    <div>
      <Link to="/create">New post</Link>
      
      <h2>Feed</h2>
      { posts.map((post: any) => {
        return (
          <Post id={post.id} title={post.name} content={post.content} publisher={post.publisher} />
        )
      }) }
    </div>
  );
}
