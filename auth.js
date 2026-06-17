const SUPABASE_URL = 'https://jwpvwosyzhtwwruphjuu.supabase.co'  // paste yours
const SUPABASE_KEY = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Imp3cHZ3b3N5emh0d3dydXBoanV1Iiwicm9sZSI6ImFub24iLCJpYXQiOjE3ODE2NjY0MjQsImV4cCI6MjA5NzI0MjQyNH0.oB8X3-q7nmO39v6CXB6tUJBUBiVHf-jwrYplUw4DVPU'                 // paste yours

const { createClient } = supabase
const supabaseClient = createClient(SUPABASE_URL, SUPABASE_KEY)