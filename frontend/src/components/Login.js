import React, { useState, useContext } from "react";
import { useNavigate } from "react-router-dom";
import axios from "axios";
import "../css/Login.css"
import { AuthContext } from "../contexts/AuthContext";

function Login() {
    const [email, setEmail] = useState("");
    const [password, setPassword] = useState("");
    const [loading, setLoading] = useState(false);
    const [error, setError] = useState(null);
    const navigate = useNavigate();
    const { login } = useContext(AuthContext);

    // Функция для отправки данных на сервер
    const handleLogin = async (e) => {
        e.preventDefault();
        setLoading(true);
        setError(null);

        try {
            // Отправляем запрос на сервер для получения токена
            const response = await axios.post("auth/login", {
                email,
                password,
            });

            // Получаем access_token из ответа
            const { access_token } = response.data;
            
            // Сохраняем токен в куки
            document.cookie = `access_token=${access_token}; path=/; max-age=3600`;
            login();
            setTimeout(() => navigate('/hotels/rooms'), 1000);
        } catch (error) {
            // Обработка ошибок
            setError("Failed to login, please check your credentials.");
            console.error("Login error:", error);
        } finally {
            setLoading(false);
        }
    };

    return (
        <div>
            <form onSubmit={handleLogin}>
                <div>
                    <label>Email:</label>
                    <input
                        type="email"
                        value={email}
                        onChange={(e) => setEmail(e.target.value)}
                        required
                    />
                </div>
                <div>
                    <label>Пароль:</label>
                    <input
                        type="password"
                        value={password}
                        onChange={(e) => setPassword(e.target.value)}
                        required
                    />
                </div>
                <div>
                    <button type="submit" disabled={loading}>
                        {loading ? "Вход..." : "Войти в аккаунт"}
                    </button>
                </div>
                {error && <p style={{ color: "red" }}>{error}</p>}
            </form>
        </div>
    );
}

export default Login;
