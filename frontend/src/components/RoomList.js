import React from "react";
import { useNavigate } from "react-router-dom";
import "../css/Rooms.css"

function RoomList({ rooms }) {
    const navigate = useNavigate();

    const handleBookingClick = (roomId) => {
        navigate('bookings/new', {state: {roomId}});
    }

    return (
        <div className="room-list-container">
            <ul className="room-list">
                {rooms.map(room => (
                    <li key={room.id} className="room-item">
                        <div>
                            <strong>Номер комнаты:</strong> {room.number}
                        </div>
                        <div>
                            <strong>Цена за ночь:</strong> {room.price} рублей
                        </div>
                        {room.description && (
                            <div>
                                <strong>Описание:</strong> {room.description}
                            </div>
                        )}
                        {room.image_url && (
                            <div>
                                <img 
                                    src={room.image_url} 
                                    alt={`Room ${room.number}`} 
                                    className="room-image"
                                />
                            </div>
                        )}
                        <button 
                            onClick={() => handleBookingClick(room.id)} 
                            className="booking-button"
                        >
                            Забронировать
                        </button>
                    </li>
                ))}
            </ul>
        </div>
    );
}

export default RoomList;