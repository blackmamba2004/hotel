import { Routes, Route } from "react-router-dom";
import About from "./components/About";
import BookingForm from "./forms/Booking";
import Login from "./components/Login";
import Logout from "./components/Logout";
import Main from "./components/Main";
import MeBookings from "./components/Bookings";
import Rooms from "./components/Rooms"; 

function App() {
  return (
    <Routes>
      <Route path="/" element={<Main />}>
        <Route path="/about" element={<About />} />
        <Route path="/hotels/rooms" element={<Rooms />} />
        <Route path="/login" element={<Login />} />
        <Route path="/logout" element={<Logout />} />
        <Route path="/bookings/me" element={<MeBookings />} />
        <Route path="hotels/rooms/bookings/new" element={<BookingForm />} />
      </Route>
    </Routes>
  );
}

export default App;
