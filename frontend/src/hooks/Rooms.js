import { useState, useEffect } from "react";
import axios from "axios";

function FetchRooms(dateFrom, dateTo) {
    const [rooms, setRooms] = useState([]);
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState(null);

    useEffect(() => {
        axios.get('/hotels/rooms', {
            params: { date_from: dateFrom, date_to: dateTo },
        })
        .then(response => {
            setRooms(response.data);
            setLoading(false);
        })
        .catch(err => {
            setError(err);
            setLoading(false);
        });
    }, [dateFrom, dateTo]);

    return { rooms, loading, error };
}

export default FetchRooms;