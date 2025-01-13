import React, { useState } from "react";
import axios from "axios";
import { useLocation, useNavigate } from "react-router-dom";
import getAccessToken from "../utils";
import '../css/BookingForm.css';

function BookingForm() {
    const access_token = getAccessToken();
    const { state } = useLocation();
    const navigate = useNavigate();
    const [formData, setFormData] = useState({
        room_id: state.roomId,
        date_from: "",
        date_to: ""
    });
    const [message, setMessage] = useState("");

    const handleChange = (e) => {
        setFormData({ ...formData, [e.target.name]: e.target.value });
    };

    const handleSubmit = async (e) => {
        e.preventDefault();
        try {
            await axios.post('/bookings', formData, {
                headers: {
                    'Authorization': 'Bearer ' + access_token
                }
            });
            setMessage("Бронь сделана!");
            setTimeout(() => navigate('/bookings/me'), 1000); // Перенаправление на главную через 3 секунды
        } catch (error) {
            console.error("Booking error:", error);
            setMessage("Ошибка при бронировании. Попробуйте снова.");
        }
    };

    return (
        <div className="booking-form-container">
            <h2>Забронировать номер</h2>
            <form onSubmit={handleSubmit}>
                <div>
                    <label>Дата заезда:</label>
                    <input
                        type="date"
                        name="date_from"
                        value={formData.date_from}
                        onChange={handleChange}
                        required
                    />
                </div>
                <div>
                    <label>Дата выезда:</label>
                    <input
                        type="date"
                        name="date_to"
                        value={formData.date_to}
                        onChange={handleChange}
                        required
                    />
                </div>
                <button type="submit">Забронировать</button>
            </form>
            {message && <p>{message}</p>}
        </div>
    );
}

export default BookingForm;
