import React, { FormEvent, useState } from "react";
import { useNavigate } from "react-router-dom";

export default (): React.ReactElement => {
  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');
  const navigate = useNavigate();
  
  const handleSubmit = async (e: FormEvent) => {
    e.preventDefault();

    const result = await fetch('http://127.0.0.1:8000/login', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({ username, password })
    });

    const json = await result.json();
    
    if (result.status !== 200) {
      window.alert(json.detail);
      return;
    }

    window.sessionStorage.setItem('token', json.token);
    navigate('/feed');
  }
  return (
    <div>
      <h2>Login page</h2>
      <form onSubmit={handleSubmit}>
      <label htmlFor='name-input'>Username:</label>
      <input id='name-input' type='text' value={username} onChange={(e) => setUsername(e.target.value)}/>
      <br/>
      <label htmlFor='name-input'>Password:</label>
      <input id='name-input' type='text' value={password} onChange={(e) => setPassword(e.target.value)}/>
      <br/>
      <input type='submit'/>
      </form>
    </div>
  );
}
