import React, { useContext } from "react";
import { Link, Outlet } from "react-router-dom";
import '../css/Main.css';
import { AuthContext } from "../contexts/AuthContext";

function Main() {
    const { isAuthenticated } = useContext(AuthContext);
    return (
        <div>
            <nav>
                <ul>
                    <li>
                        <Link to="/hotels/rooms">Номера</Link>
                    </li>
                    {isAuthenticated ? (
                        <li>
                            <Link to="/bookings/me">Мои бронирования</Link>
                            <Link to="/logout"> Выйти</Link>
                        </li>
                    ) : (
                        <li>
                            <Link to="/login">Войти</Link>
                        </li>
                    )}
                    <li>
                        <Link to="/about">О проекте</Link>
                    </li>
                </ul>
            </nav>
            <main>
                <Outlet />
            </main>
        </div>
    );
}

export default Main;
