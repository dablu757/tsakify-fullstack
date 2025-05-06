function LoginPage() {
  return (
    <div className="login-container">
      
      <div className="login-card">

        <h2 className="login-title">Login to Your Account</h2>

        <form className="login-form">

          <div>
            <input
              type="email"
              placeholder="Enter Email"
              className="login-input"
              required
            />
          </div>

          <div>
            <input
              type="password"
              placeholder="Enter Password"
              className="login-input"
              required
            />
          </div>

          <button type="submit" className="login-button">Submit</button>
        </form>

        <p className="login-footer">
          Don’t have an account?
          <a href="/register" className="login-link">Register</a>
        </p>

      </div>
    </div>
  );
}

export default LoginPage;
