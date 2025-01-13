import { useEffect, useState } from "react";
import axios from "axios";
import getAccessToken from "../utils"

function FetchMeBookings() {
    const [bookings, setBookings] = useState([]);
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState(null);

    useEffect(() => {
        const access_token = getAccessToken();
        axios.get('/bookings/me', {
            headers: {
                'Authorization': 'Bearer ' + access_token
            }
        })
        .then(response => {
            setBookings(response.data);
            setLoading(false);
        })
        .catch(err => {
            setError(err);
            setLoading(false);
        });
    }, []);

    return { bookings, loading, error };
}

export default FetchMeBookings;