INSERT INTO hotel (name, location, image_url) VALUES 
('Cosmos Collection Altay Resort', 'Республика Алтай, Майминский район, село Урлу-Аспак, Лесхозная улица, 20', 'static/images/hotels/1.jpg'),
('Skala', 'Республика Алтай, Майминский район, поселок Барангол, Чуйская улица 40а', 2),
('Ару-Кёль', 'Республика Алтай, Турочакский район, село Артыбаш, Телецкая улица, 44А', 3),
('Гостиница Сыктывкар', 'Республика Коми, Сыктывкар, Коммунистическая улица, 67', 4),
('Palace', 'Республика Коми, Сыктывкар, Первомайская улица, 62', 5),
('Bridge Resort', 'посёлок городского типа Сириус, Фигурная улица, 45', 6);

INSERT INTO room (id, hotel_id, number, description, price, image_url) VALUES
(1, 1, 101, 'Номер с видом на горы.', 24500, 'static/images/rooms/1.jpg'),
(2, 1, 102, 'Шикарный номер с видом на озеро', 22450, 'static/images/rooms/2.jpg'),
(3, 1, 201, 'Номер с видом на океан.', 4570, 'static/images/rooms/3.jpg'),
(4, 1, 202, 'Номер с видом на гору Тухтала.', 4350, 'static/images/rooms/4.jpg'),
(5, 1, 301, 'Красивый номер для всей семьи.', 7080, 'static/images/rooms/5.jpg'),
(6, 1, 302, 'Красивый номер для молодоженов.', 9815, 'static/images/rooms/6.jpg'),
(7, 1, 401, 'Стандартный номер для стандартных людей.', 4300, 'static/images/rooms/7.jpg'),
(8, 1, 402, 'Номер для бурной вечеринки вдвоем.', 4700, 'static/images/rooms/8.jpg'),
(9, 1, 501, 'Вкусный завтрак и мягкий матрас - рецепт хорошего отдыха.', 5000, 'static/images/rooms/9.jpg'),
(10, 1, 502, 'Полулюкс - он и есть полулюкс, шик и блеск.', 8000, 'static/images/rooms/10.jpg'),
(11, 1, 601, 'Стандартный номер.', 8125, 'static/images/rooms/11.jpg');

INSERT INTO 'user' (first_name, last_name, patronymic, email, hashed_password, gender, is_active, is_superuser) VALUES 
('Васильев', 'Семен', 'Дмитриевич', 'aa@aa.ru', 'hashed_password_1', 'MALE', 'true', 'true'),
('Киселев', 'Никита', 'Константинович', 'kk@kk.ru', 'hashed_password_2', 'MALE', 'true', 'false');

INSERT INTO booking (room_id, user_id, date_from, date_to) VALUES
(1, 1, '2023-06-15', '2023-06-30'),
(7, 2, '2023-06-25', '2023-07-10');