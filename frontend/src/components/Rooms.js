import React, { useState } from "react";
import FetchRooms from "../hooks/Rooms";
import RoomList from "./RoomList";

function Rooms() {
    const [dateFrom, setDateFrom] = useState("2025-01-01");
    const [dateTo, setDateTo] = useState("2025-01-03");
    const [submitted, setSubmitted] = useState(false);
    const { rooms, loading, error } = FetchRooms(dateFrom, dateTo);

    // Обработчик изменения дат
    const handleDateFromChange = (e) => {
        setDateFrom(e.target.value);
        setSubmitted(false); // Чтобы не перерисовывать, пока не нажмем кнопку
    };

    const handleDateToChange = (e) => {
        setDateTo(e.target.value);
        setSubmitted(false); // Чтобы не перерисовывать, пока не нажмем кнопку
    };

    // Обработчик отправки фильтров
    const applyFilters = () => {
        setSubmitted(true);
    };

    return (
        <div>
            <div className="filters">
                <label>Дата заезда:</label>
                <input
                    type="date"
                    value={dateFrom}
                    onChange={handleDateFromChange}
                    min="2025-01-01"
                    // max="2025-12-31"
                />

                <label>Дата выезда:</label>
                <input
                    type="date"
                    value={dateTo}
                    onChange={handleDateToChange}
                    min="2025-01-02"
                    // max="2025-12-31"
                />

                <button onClick={applyFilters}>Применить фильтры</button>
            </div>

            {/* Состояния загрузки и ошибок */}
            {submitted && (
                <>
                    {loading && <p>Loading...</p>}
                    {error && <p>Error: {error.message}</p>}
                    {!loading && !error && <RoomList rooms={rooms} />}
                </>
            )}
        </div>
    );
}

export default Rooms;
