import { useEffect, useContext } from "react";
import { useNavigate } from "react-router-dom";
import { AuthContext } from "../contexts/AuthContext";

function Logout() {
    const navigate = useNavigate();
    const { logout } = useContext(AuthContext);

    useEffect(() => {
        document.cookie = "access_token=; path=/; max-age=0";

        logout();

        navigate("/login");
    }, [logout, navigate])

    return null;
}

export default Logout;