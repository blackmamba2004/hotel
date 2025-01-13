import React, { useState } from "react";
import axios from "axios";
import '../css/Bookings.css'; // Подключение CSS
import getAccessToken from "../utils";

function BookingList({ bookings }) {
    const [updatedBookings, setUpdatedBookings] = useState(bookings);
    const access_token = getAccessToken();
    const handleDelete = async (bookingId) => {
        try {
            // Отправка запроса на удаление
            await axios.delete(`/bookings/${bookingId}`, {
                headers: {
                    'Authorization': 'Bearer ' + access_token
                }
            });
            // Обновление списка бронирований
            setUpdatedBookings(updatedBookings.filter(booking => booking.id !== bookingId));
        } catch (error) {
            console.error("Error deleting booking:", error);
        }
    };
    return (
        <div className="booking-list-container">
            {updatedBookings.length === 0 ? (
                <p>У вас нет бронирований.</p>
            ) : (
                <ul className="booking-list">
                    {updatedBookings.map(booking => (
                        <li key={booking.id} className="booking-item">
                            <div className="booking-details">
                                <p>
                                    <strong>Заезд:</strong> {new Date(booking.date_from).toLocaleDateString()}
                                </p>
                                <p>
                                    <strong>Выезд:</strong> {new Date(booking.date_to).toLocaleDateString()}
                                </p>
                                <p>
                                    <strong>Цена:</strong> {booking.price} рублей
                                </p>
                                <button 
                                    onClick={() => handleDelete(booking.id)} 
                                    className="delete-button"
                                >
                                    Удалить
                                </button>
                            </div>
                        </li>
                    ))}
                </ul>
            )}
        </div>
    );
}

export default BookingList;
