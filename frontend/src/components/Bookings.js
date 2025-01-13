import FetchMeBookings from "../hooks/Bookings";
import BookingList from "../pages/Bookings";

function MeBookings() {
    const { bookings, loading, error } = FetchMeBookings();

    if (loading) return <p>Loading...</p>
    if (error) return <p>Error: {error.message}</p>

    return <BookingList bookings={bookings} />
}

export default MeBookings;