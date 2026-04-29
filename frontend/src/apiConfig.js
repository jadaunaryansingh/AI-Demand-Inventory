/** API base URL: set VITE_API_URL in Render (or .env) to your deployed FastAPI origin, no trailing slash. */
export const getApiBaseUrl = () => {
  const env = import.meta.env.VITE_API_URL;
  if (env && String(env).trim()) return String(env).replace(/\/$/, '');
  return 'http://localhost:8000';
};
