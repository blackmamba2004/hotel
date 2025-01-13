import React from "react";
import "../css/About.css"; // Подключение CSS стилей

function About() {
    return (
        <div className="about-container">
            <p>В этом проекте используются следующие технологии:</p>
            <ul className="tech-list">
                <li>FastAPI</li>
                <li>SqlAlchemy</li>
                <li>Alembic</li>
                <li>PostgreSQL</li>
                <li>Docker</li>
                <li>React</li>
                <li>Axios</li>
                <li>React Router</li>
                <li>CSS Modules</li>
            </ul>
        </div>
    );
}

export default About;