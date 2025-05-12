import { useEffect, useState } from "react";

function LoginPage() {
  const [status, setStatus] = useState();
  const [userLoggedIn, setUserLoggedIn] = useState(false);
  // check localstorage is there or not
  const userToken = localStorage.getItem('userToken');

  // useEffect()

  // store session in local storage
  const handleLoginSuccess = (token)=>{
    localStorage.setItem('userToken',token);

  };

  // on submit action
  const onSubmitForm = async (event) => {
    event.preventDefault();
    const myHeaders = new Headers();
    myHeaders.append("Content-Type", "application/json");

    const result = await fetch("http://127.0.0.1:8080/auth/login", {
      method: "POST",
      headers: myHeaders,
      body: JSON.stringify({
        email: event.target[0].value,
        password: event.target[1].value,
      }),
    });
    var respose = await result.json();

    if (respose.status=="success"){
      // const _token = respose.data.access_token
      // const _refresh_tocken = respose.data.refresh_token
      // JSON.stringify(respose.data)
      handleLoginSuccess(JSON.stringify(respose.data))
    }

    console.log(respose);
    setStatus(respose.message);
  };


  return (
    <div className="login-container">
      <div className="login-card">
        <h2 className="login-title">Login to Your Account</h2>
        {status && <div style={{
          color:'#000',
          marginBottom: 10
        }} >{status}</div>}
        <form onSubmit={onSubmitForm} className="login-form">
            <input
              type="email"
              placeholder="Enter Email"
              className="login-input"
              name="email"
              required
            />

            <input
              type="password"
              placeholder="Enter Password"
              className="login-input"
              name="password"
              required
            />

          <button type="submit" className="login-button">
            Submit
          </button>
        </form>

        <p className="login-footer">
          Don’t have an account?
          <a href="/register" className="login-link">
            Register
          </a>
        </p>
      </div>
    </div>
  );
}

export default LoginPage;




// import { useState } from "react";

// function LoginPage() {
//   const [status, setStatus] = useState("");

//   const handleLoginSuccess = (token) => {
//     localStorage.setItem("userToken", token);
//     setStatus("Login successful!");
//     // You can also redirect here using React Router if needed
//   };

//   const onSubmitForm = async (event) => {
//     event.preventDefault();

//     const myHeaders = new Headers();
//     myHeaders.append("Content-Type", "application/json");

//     const response = await fetch("http://127.0.0.1:8080/auth/login", {
//       method: "POST",
//       headers: myHeaders,
//       body: JSON.stringify({
//         email: event.target.email.value,
//         password: event.target.password.value,
//       }),
//     });

//     const result = await response.json();

//     if (response.ok && result.token) {
//       handleLoginSuccess(result.token);
//     } else {
//       setStatus(result.message || "Login failed.");
//     }
//   };

//   return (
//     <div className="login-container">
//       <div className="login-card">
//         <h2 className="login-title">Login to Your Account</h2>

//         {status && (
//           <div style={{ color: "#000", marginBottom: 10 }}>{status}</div>
//         )}

//         <form onSubmit={onSubmitForm} className="login-form">
//           <input
//             type="email"
//             placeholder="Enter Email"
//             className="login-input"
//             name="email"
//             required
//           />
//           <input
//             type="password"
//             placeholder="Enter Password"
//             className="login-input"
//             name="password"
//             required
//           />
//           <button type="submit" className="login-button">
//             Submit
//           </button>
//         </form>

//         <p className="login-footer">
//           Don’t have an account?
//           <a href="/register" className="login-link">
//             Register
//           </a>
//         </p>
//       </div>
//     </div>
//   );
// }

// export default LoginPage;
