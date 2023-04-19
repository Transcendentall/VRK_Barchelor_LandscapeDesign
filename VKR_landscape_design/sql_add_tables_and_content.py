import sqlite3
import pandas as pd

# PRAGMA FOREIGN_KEYS = on;

con = sqlite3.connect("VKR.sqlite")

con.executescript('''

CREATE TABLE IF NOT EXISTS users(
    user_id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_login VARCHAR(20) NOT NULL,
    user_password VARCHAR(30) NOT NULL,
    user_FIO VARCHAR(50) NOT NULL,
    user_email VARCHAR(30) NOT NULL,
    user_isAdmin BOOLEAN NOT NULL
 );

CREATE TABLE IF NOT EXISTS territories(
    territorie_id INTEGER PRIMARY KEY AUTOINCREMENT,
    territorie_coord_x REAL NOT NULL,
    territorie_coord_y REAL NOT NULL,
    territorie_coord_z REAL NOT NULL
 );
CREATE TABLE IF NOT EXISTS soils(
    soil_id INTEGER PRIMARY KEY AUTOINCREMENT,
    soil_name VARCHAR(30) NOT NULL,
    soil_description VARCHAR(250) NOT NULL,
    soil_acidity REAL,
    soil_minerals VARCHAR(50),
    soil_profile VARCHAR(50)
 );
CREATE TABLE IF NOT EXISTS grounds(
    ground_id INTEGER PRIMARY KEY AUTOINCREMENT,
    ground_name VARCHAR(50) NOT NULL,
    ground_description VARCHAR(500) NOT NULL,
    ground_density REAL,
    ground_humidity REAL,
    ground_hardness_Moos REAL
 );
CREATE TABLE IF NOT EXISTS plants(
    plant_id INTEGER PRIMARY KEY AUTOINCREMENT,
    plant_name VARCHAR(30) NOT NULL,
    plant_description VARCHAR(500) NOT NULL,
    plant_isFodder BOOLEAN NOT NULL,
    plant_isExactingToTheLight BOOLEAN,
    plant_isOneYear BOOLEAN,
    plant_isTwoYears BOOLEAN,
    plant_isManyYears BOOLEAN,
    plant_climat VARCHAR(30),
    plant_required_minerals_and_trace_elements VARCHAR(100),
    plant_temperature_min INTEGER,
    plant_temperature_max INTEGER,
    plant_kingdom VARCHAR(20),
    plant_departament VARCHAR(20),
    plant_class VARCHAR(20),
    plant_order VARCHAR(20),
    plant_family VARCHAR(20),
    plant_genus VARCHAR(20),
    plant_species VARCHAR(20)
 );
CREATE TABLE IF NOT EXISTS animals(
    animal_id INTEGER PRIMARY KEY AUTOINCREMENT,
    animal_name VARCHAR(30) NOT NULL,
    animal_description VARCHAR(250) NOT NULL,
    animal_kingdom VARCHAR(20),
    animal_philum VARCHAR(20),
    animal_class VARCHAR(20),
    animal_order VARCHAR(20),
    animal_family VARCHAR(20),
    animal_genus VARCHAR(20),
    animal_species VARCHAR(20)
 );

CREATE TABLE IF NOT EXISTS connection_territories_soils(
    connection_territories_soils_id INTEGER PRIMARY KEY AUTOINCREMENT,
    connection_territorie_id INTEGER NOT NULL,
    connection_soil_id INTEGER NOT NULL
 );
CREATE TABLE IF NOT EXISTS connection_soils_grounds(
    connection_soils_grounds_id INTEGER PRIMARY KEY AUTOINCREMENT,
    connection_soil_id INTEGER NOT NULL,
    connection_ground_id INTEGER NOT NULL
 );
CREATE TABLE IF NOT EXISTS connection_soils_plants(
    connection_soils_plants_id INTEGER PRIMARY KEY AUTOINCREMENT,
    connection_soil_id INTEGER NOT NULL,
    connection_plant_id INTEGER NOT NULL,
    connection_soils_plants_isGood BOOLEAN
 );
CREATE TABLE IF NOT EXISTS connection_plants_animals(
    connection_plants_animals_id INTEGER PRIMARY KEY AUTOINCREMENT,
    connection_plant_id INTEGER NOT NULL,
    connection_animal_id INTEGER NOT NULL
 );



INSERT INTO users (user_login, user_password, user_FIO, user_email, user_isAdmin)
VALUES
('root', 'samyyslozhnyyparolvmire12345!!!', 'Иванов Пётр Сидорович', 'superadmin@yandex.ru', True),
('vanek2002', '12345abcde', 'Иванов Иван Иванович', 'vanya@yandex.ru', False),
('petrpervuy', '!qwerty15', 'Петров Пётр Петрович', 'petrpervuy@gmail.com', False),
('lutiysidor', 'abracadabra123', 'Сидоров Сидр Сидорович', 'supersid@mail.ru', False);


INSERT INTO territories (territorie_coord_x, territorie_coord_y, territorie_coord_z)
VALUES
(43.038126, 131.884906, 41),
(43.027650, 131.895167, 18);
INSERT INTO territories (territorie_coord_x, territorie_coord_y, territorie_coord_z)
VALUES
(43.078497, 131.944396, 35),
(43.093035, 131.912163, 41),
(43.093788, 131.951451, 62);

INSERT INTO soils (soil_name, soil_description, soil_profile)
VALUES
('Бурые лесные слабоненасыщенные оподзоленные (буроземы слабоненасыщенные оподзоленные)', 'По химическим свойствам (кислотности, ненасыщенности, емкости поглощения и составу гумуса) близки к бурым лесным слабоненасыщенным почвам. Отличаются от последних некоторой цветовой и текстурной дифференциацией профиля, а также наличием слабого перераспределения по профилю валовых и подвижных (аморфных и окристаллизованных) форм R2O3. Ареал распространения — юг Дальнего Востока.', 'О1—АО—А1—А1А2—Вm,t—BmC—С'),
('Дерново-палево-подзолистые и подзолисто-буроземные', 'Формируются как на однородных суглинистых породах, так и на двучленных породах (легкие суглинки, супеси и пески, подстилаемые тяжелыми бескарбонатными суглинками и глинами). Характерны: резко выраженная цветная и текстурная дифференциация профиля и иногда поверхностное оглеение, сочетающееся с процессами оподзоливания. Верхний органогенный горизонт О (2–3 см) сменяется маломощным (2–5 см) горизонтом АО. Гумусовый горизонт А1f (5–10см) серовато-палевый или серовато-светло-бурый, комковатый, слабо уплотнен. Оподзоленный горизонт A2g,n(A2) комковатый или чешуйчато-плитчатый, несколько обеднен оксидами железа, обогащен (по сравнению с породой) аморфными и окристаллизованными формами R2O3, содержит большое количество сегрегированных в микроконкреции органо-железистых новообразований, иногда глееватость морфологически не обнаруживается. Горизонт A2/Btg белесовато-сизоватый, плотный, сильно варьирует по мощности. Образует глубокие белесые языки и карманы, проникающие в горизонт Bt. По сравнению с вышележащим горизонтом, горизонт A2/Btg несколько обогащен валовым железом и обеднен оксалаторастворимыми формами железа и алюминия; иногда глееватость морфологически не обнаруживается. Горизонт Bt плотный, глинистый или тяжелосуглинистый, ореховато-призматический, с темными марганцовистыми лакировками, несколько обогащен R2O3 и илистой фракцией, постепенно через горизонт BtC переходит в почвообразующую породу. Реакция почв кислая, биогенная аккумуляция слабая, содержание гумуса низкое (2–4%). Гумус фульватный, ненасыщенный, с незначительным количеством свободных фульвокислот, отношение С:N узкое; при общем элювиально-иллювиальном распределении R2O3 и кремнезема по профилю ход изменения аморфных (оксалаторастворимых) форм железа и алюминия имеет аккумулятивный характер. Основные ареалы — Псковская, Новгородская, Смоленская области, Дальний Восток. Формируются под хвойно-широколиственными и широколиственными, мертвопокровными и травяными лесами.', 'О—AO—A1f—A2g,n(A2)—A2/Btg(A2Bt)—Bt—BtC—С'),
('Бурые лесные слабоненасыщенные (буроземы слабоненасыщенные)', 'Отличаются от бурых лесных кислых по химическим свойствам: слабокислой реакцией (рН сол 4,5–6,0), значительно большими насыщенностью (40–60%) поглощающего комплекса основаниями и емкостью поглощения (12–20 мг-экв) и несколько иным составом органического вещества, заметным участием в составе гуминовых кислот фракции, связанной с Са.', 'A1—Bm—C');

INSERT INTO animals (animal_name, animal_description, animal_kingdom, animal_philum, animal_class, animal_order, animal_family, animal_genus, animal_species)
VALUES
('Свиньи', 'Домашняя свинья (лат. Sus domesticus, или Sus scrofa domesticus) — крупное парнокопытное млекопитающее животное рода кабанов (свиней), одомашненное человеком около 7 тыс. лет назад (по некоторым исследованиям — значительно раньше) и распространённое главным образом в странах Запада, в Восточной Азии и в Океании. Одичавшие свиньи (рейзорбеки) встречаются в Северной Америке, в Австралии и в Новой Зеландии. Длина тела составляет от 0,9 до 1,8 м, взрослая особь весит от 50 до 150 кг. По сравнению с другими парнокопытными, которые чаще бывают растительноядными, домашняя свинья всеядна, как и её предок, дикий кабан. Свиньи выращиваются в основном ради мяса и сала. Мировое производство свинины в 2005 году составило 97,2 млн т (по данным Министерства сельского хозяйства США).', 'Животные', 'Хордовые', 'Млекопитающие', 'Китопарнокопытные', 'Свиные', 'Кабаны', 'Домашняя свинья'),
('Овцы', 'Домашняя овца (лат. Ovis aries) — парнокопытное млекопитающее из рода баранов, семейства полорогих. Это животное уже в глубокой древности было одомашнено человеком, в основном из-за густой шерсти и съедобного мяса. В настоящее время стриженая овечья шерсть, или руно, используется человеком чаще, чем шерсть любого другого животного. Овечье мясо, называемое бараниной, является одним из важнейших продуктов потребления во многих странах мира. Помимо шерсти и мяса, овец разводят для получения овечьего молока, которое используется для изготовления сыра, а также кулинарного жира и шкур (овчины). Наконец, овцы используются в научных экспериментах: одним из известнейших представителей этого вида считается овечка Долли — первое в мире клонированное млекопитающее (в 1996 году). В узком смысле под овцами подразумевают самок домашней овцы, тогда как самцов обычно называют баранами. Молодые самки, не достигшие половой зрелости, именуются ярками, а потомство — ягнятами. Овцеводство — отрасль животноводства, занимающаяся разведением овец — практикуется во всём мире и во все времена играла важную роль в экономике многих стран. В настоящее время наибольшее поголовье овец имеется в Китае (около 144 млн голов), Австралии (98 млн), Индии (ок. 60 млн), Иране (54 млн), Новой Зеландии (44 млн), Великобритании (36 млн), ЮАР (св. 29 млн), Турции (27 млн), Пакистане и Испании (по 24 млн). В постсоветских странах овцеводство наиболее значимо как отрасль животноводства в Киргизии, Казахстане, Туркмении, Молдавии и юге России.', 'Животные', 'Хордовые', 'Млекопитающие', 'Китопарнокопытные', 'Полорогие', 'Бараны', 'Домашняя овца'),
('Лошади', 'Домашняя лошадь (лат. Equus caballus, или Equus ferus caballus) — животное из семейства лошадиных отряда непарнокопытных, одомашненный потомок дикой лошади (Equus ferus). Используется человеком вплоть до настоящего времени. Лошади (Equus) в широком смысле слова — единственный ныне живущий род семейства лошадиных (Equidae) отряда непарнокопытных (Perissodactyla). Наиболее характерную особенность лошадиных составляют ноги, имеющие только один вполне развитый и одетый копытом палец. Череп вытянут и отличается относительно длинной лицевой частью. Долгое время лошади были в числе экономически наиболее важных для человека домашних животных, однако их важность упала в связи с развитием механизации. Самец лошади называется жеребцом, или (в просторечии) конём. Самка — кобылой. Кастрированный жеребец называется мерином. Детёныш лошади — жеребёнком. В природе лошадь — житель больших, открытых пространств степей или прерий, спасающаяся в случае опасности при помощи бегства. Наука, изучающая лошадей, называется иппологией. Помещение для содержания одомашненной лошади называется конюшней.', 'Животные', 'Хордовые', 'Млекопитающие', 'Непарнокопытные', 'Лошадиные', 'Лошади', 'Домашняя лошадь'); 

INSERT INTO plants (plant_name, plant_description, plant_isFodder, plant_isExactingToTheLight, plant_isOneYear, plant_isTwoYears, plant_isManyYears, plant_climat, plant_temperature_min, plant_temperature_max, plant_kingdom, plant_departament, plant_class, plant_order, plant_family, plant_genus, plant_species)
VALUES
('Картофель', 'Картофель, или паслён клубненосный (лат. Solanum tuberosum), — вид многолетних клубненосных травянистых растений из рода Паслён (Solanum) семейства Паслёновые (Solanaceae). Клубни картофеля являются важным пищевым продуктом. Плоды ядовиты в связи с содержанием в них соланина. С потребительской точки зрения картофель является овощем. Картофель размножают вегетативно — небольшими клубнями или частями клубней (и для целей селекции — семенами или листоклубнями(черенкованием)). Они высаживаются на глубину от 5 до 10 см. Прорастание почек клубней в почве начинается при 5-8 °C (оптимальная температура для прорастания картофеля 15-20 °C). Для фотосинтеза, роста стеблей, листьев и цветения — 16-22 °C. Наиболее интенсивно клубни образуются при ночной температуре воздуха 10-13 °C. Высокая температура (ночная около 20 °C и выше) вызывает тепловое вырождение. Из семенных клубней развиваются растения с резко пониженной продуктивностью. Всходы и молодые растения повреждаются при заморозках в −2 °C. Транспирационный коэффициент картофеля в среднем 400—500. Наибольшее количество воды растение потребляет во время цветения и клубнеобразования. Картофель требователен к режиму полива, избыток влаги для него вреден. На формирование надземной части и клубней расходуется много питательных веществ, особенно в период максимальных приростов вегетативной массы и начала клубнеобразования. При урожае 200—250 ц с 1 га растения извлекают из почвы 100—175 кг азота, 40-50 кг фосфора и 140—230 кг калия. Лучшие для картофеля почвы — чернозёмы, дерново-подзолистые, серые лесные, осушенные торфяники; по механическому составу — супеси, лёгкие и средние суглинки. Для картофеля желательна рыхлая почва. При хорошей обработке почвы и правильном применении удобрений картофель даёт высокие урожаи даже при длительном выращивании на одном и том же месте. Картофель отзывчив на внесение удобрений. Лучшими удобрениями служат калийные соли, затем костная мука, известь, перепревший навоз (не кислый, например, в смеси с той же известью). Избыток азотных удобрений в почве нежелателен, так как это способствует разрастанию ботвы в ущерб образованию клубней.', FALSE, TRUE, FALSE, FALSE, TRUE, 'умеренно-прохладный', 14, 18, 'Растения', 'Цветковые', 'Двудольные', 'Паслёноцветные', 'Паслёновые', 'Паслён', 'Картофель обыкновенный (паслён клубненосный)'),
('Огурец', 'Огурец обыкновенный, или Огурец посевной (лат. Cucumis sativus), — однолетнее травянистое растение, вид рода Огурец (Cucumis) семейства Тыквенные (Cucurbitaceae), овощная культура. Стебель — стелющийся, шершавый, заканчивается усиками, которыми он может зацепиться за опору, вытянувшись при этом на 1—2 м. Растение также может расстилаться по земле, если у него нет опор. Листья сердцевидные, пятилопастные. Плод — многосемянный, сочный, изумрудно-зелёный, плотный, пупырчатый, в естественной среде также с мелкими колючками (искусственно выведены плоды с гладким внеплодником. Строение плода характерно для семейства Тыквенных и в ботанической литературе определяется как тыквина. Он может иметь различную форму и размер (в зависимости от сорта). В кулинарном отношении огурцы традиционно относятся к популярным овощам. Геном огурца посевного был полностью расшифрован в 2009 году; он насчитывает 350 миллионов пар оснований ДНК. Пять из семи хромосом огурцов возникли из десяти хромосом общих предков с дыней.', FALSE, TRUE, TRUE, FALSE, FALSE, 'умеренный', 17, 35, 'Растения', 'Цветковые', 'Двудольные', 'Тыквоцветные', 'Тыквенные', 'Огурец', 'Огурец обыкновенный (огурец посевной)'),
('Помидор', 'Томат, или помидор (лат. Solanum lycopersicum) — однолетнее или многолетнее травянистое растение, вид рода Паслён (Solanum) семейства Паслёновые (Solanaceae). Возделывается как овощная культура; выращивается ради съедобных плодов — сочных многогнёздных ягод различной формы и окраски, также называемых томатами или помидорами. Томат имеет сильно развитую корневую систему стержневого типа. Корни разветвлённые, растут и формируются быстро. Уходят в землю на большую глубину (при безрассадной культуре до 1 м и более), распространяясь в диаметре на 1,5—2,5 м. При наличии влаги и питания дополнительные корни могут образовываться на любой части стебля, поэтому томат можно размножать не только семенами, но также черенками и боковыми побегами (пасынками). Поставленные в воду, они через несколько суток образуют корни. Стебель у томата прямостоячий или полегающий, ветвящийся, высотой от 30 см до 2 м и более. Листья непарноперистые, рассечённые на крупные доли, иногда картофельного типа. Цветки мелкие, невзрачные, жёлтые различных оттенков, собраны в кисть. Томат — факультативный самоопылитель: в одном цветке имеются мужские и женские органы. Плоды — сочные многогнёздные ягоды различной формы (от плоско-округлой до цилиндрической; могут быть мелкими (масса до 50 г), средними (51—100 г) и крупными (свыше 100 г, иногда до 800 г и более). Окраска плодов от бледно-розовой до ярко-красной и малиновой, от белой, светло-зелёной, светло-жёлтой до золотисто-жёлтой.', FALSE, TRUE, TRUE, FALSE, TRUE, 'тёплый', 15, 20, 'Растения', 'Цветковые', 'Двудольные', 'Паслёноцветные', 'Паслёновые', 'Паслён', 'Томат (помидор)'),
('Клевер', 'Клевер луговой, или клевер красный (лат. Trifolium pratense), — растение из рода Клевер (Trifolium), семейства Бобовые (Fabaceae), подсемейства Мотыльковые (Faboideae). Ценное кормовое и пастбищное растение. Клевер луговой — двулетнее, но чаще многолетнее травянистое растение. Корень стержневой или стержнемочковатый, сильно ветвящийся, проникает в почву на глубину до 2 м. Боковые сильно разветвлённые мочковатые корни распределяются в пахотном слое почвы. Наибольшее их количество расположено в слое глубиной до 10 см. В целом глубина проникновения зависит от особенностей почвы, распределения в ней питательных веществ, влаги и залегания грунтовых вод. На корнях формируются клубеньки. Стебли прямостоячие, восходящие и стелющиеся, высотою 40—65 см (в травосмесях и опытных посевах 1 м, иногда до 2 м), толстые или тонкие, голые или слабоопушенные. В зависимости от типа, сорта, условия произрастания в кусте бывает в среднем 5—8 стеблей в густых посевах и 30—70 в разреженных. Каждый стебель состоит из 8—10 междоузлий размером 10—20 см. Листья тройчатые, с широкояйцевидными мелкозубчатыми долями, листочки по краям цельные, с нежными ресничками по краям. Соцветия-головки рыхлые, шаровидные, сидят часто попарно и нередко прикрыты двумя верхними листьями. Венчик красный, изредка белый или неодноцветный; чашечка с десятью жилками. Плод — яйцевидный, односемянный боб; семена то округлые, то угловатые, то желтовато-красные, то фиолетовые. Масса 1000 семян 1,5—2 грамма. Цветёт в июне-сентябре. Плоды созревают в августе-октябре. Размножается как семенами, так и вегетативно.', TRUE, TRUE, TRUE, TRUE, TRUE, 'умеренно-влажный', 1, 20, 'Растения', 'Цветковые', 'Двудольные', 'Бобовоцветные', 'Бобовые', 'Клевер', 'Клевер луговой'),
('Люцерна', 'Люцерна посевная, люцерна синяя (лат. Medicago sativa) — травянистое растение; типовой вид рода Люцерна (Medicago) семейства Бобовые (Fabaceae). Широко применяется как кормовое растение. В диком виде произрастает в Малой Азии и на Балканах. В культуре и как заносное — по всему миру. Растение произрастает по осыпям, на сухих лугах, травянистых склонах, на степях, на пастбищах, по опушкам, в кустарниках, на галечниках, в долинах рек, как сорное, в посевах и около них. Стебли четырёхгранные, голые или опушённые, в верхней части сильно ветвящиеся, до 80 см высотой, могут быть прямыми, широко кустистыми или лежащими. Корневище мощное, толстое, глубоко залегающее. Листья на черешках. Листочки 1—2 см длиной и 0,3—1 см шириной, продолговато-обратнояйцевидные, цельные. Цветоносы пазушные, длиннее листьев. Кисть головчатая, густая, многоцветковая, 2—3 см длиной. Цветки сине-фиолетовые. Чашечка 0,5—0,6 см длиной трубчато-воронковидная, волосистая. Плод — боб, около 0,6 см в поперечнике.', TRUE, TRUE, TRUE, FALSE, TRUE, 'тёплый и светлый', 22, 30, 'Растения', 'Цветковые', 'Двудольные', 'Бобовоцветные', 'Бобовые', 'Люцерна', 'Люцерна посевная');
INSERT INTO plants (plant_name, plant_description, plant_isFodder, plant_isExactingToTheLight, plant_climat, plant_temperature_min, plant_temperature_max, plant_kingdom, plant_departament, plant_class, plant_order, plant_family, plant_genus, plant_species)
VALUES
('Шампиньон', 'Шампиньон (лат. Agaricus) — род пластинчатых грибов семейства Шампиньоновые (Агариковые) (лат. Agaricaceae). Русское название «шампиньон» происходит от фр. champignon, означающего просто «гриб». Род включает в себя как съедобные, так и несъедобные грибы. К числу культивируемых съедобных относится шампиньон двуспоровый. Плодовые тела различных размеров — от 3—5 (Agaricus comtulus) до 20—25 см (Agaricus arvensis). Шляпка массивная, плотная, сначала округлая, с возрастом становится всё более плоской. Поверхность гладкая, либо покрыта тёмными чешуйками; цвет — от белого до буроватого и коричневого. Пластинки свободные, вначале белые, затем темнеют, изменяя окраску от розоватого до почти чёрного цвета, что обусловлено изменением окраски спор. По этому признаку шампиньоны легко отличить от похожих на них ядовитых грибов рода Amanita, у которых в течение всей жизни плодового тела пластинки и споры остаются белыми, либо желтоватыми. Ножка центральная, ровная, плотная, реже рыхлая или полая внутри. Всегда имеется частное покрывало, оставляющее на ножке хорошо заметное одно- или двухслойное кольцо. Мякоть — различных оттенков белого цвета. На воздухе часто приобретает желтоватый или красноватый оттенок. Обычно имеет выраженный «грибной» либо «анисовый» запах.', FALSE, FALSE, 'умеренно-континентальный', 16, 24, 'Грибы', 'Базидиомицеты', 'Агарикомицеты', 'Агариковые', 'Шампиньоновые', 'Шампиньон', 'Шампиньон обыкновенный');

INSERT INTO grounds (ground_name, ground_description)
VALUES
('Песчаный', 'Песчаный грунт отличается рыхлостью, легкостью, сыпучестью, он легко пропускает воздух, воду, тепло и подкормки к корням растений, однако эти достоинства одновременно являются и недостатками: песчаные грунты быстро высыхают, остывают, а питательные вещества легко из них вымываются. Чтобы повысить плодородность песчаного грунта, необходимо регулярно вносить в него уплотняющие и связующие вещества: торф, перегной, компост, выращивать и заделывать в грунт сидераты, проводить мульчирование поверхности.'),
('Супесчаный', 'Этот грунт по механическому составу тоже считается легким, но он содержит в себе некоторое количество глины, поэтому лучше удерживает воздух, воду и питательные вещества, хорошо прогревается и не так быстро остывает. Супесчаный грунт легко обрабатывать, а выращивать на нем можно практически любую культуру, однако желательно поддерживать плодородность внесением органики, выращиванием и заделкой сидератов и регулярным мульчированием.'),
('Глинистый', 'Этот тяжёлый грунт плохо поддается обработке, очень долго сохнет и греется. Как правило, глинистый грунт имеет кислую реакцию, плохо пропускает питание, тепло, влагу и воздух к корням растений, в нем нет условий для развития полезных микроорганизмов, а растительные остатки в глине очень долго разлагаются. Из-за того, что глинистый грунт долго высыхает после таяния снега и медленно прогревается, посадку культур приходится задерживать. Чтобы улучшить состав грунта, в него нужно вносить под перекопку крупнозернистый песок, торф и перегной, а для нейтрализации кислой реакции глинистую почву нужно один раз в три года известковать.'),
('Суглинистый', 'Для выращивания садово-огородных культур суглинок является одним из лучших грунтов: он питателен, тепло-, водо- и воздухопроницаем, его легко обрабатывать. Главное, его нет необходимости улучшать, нужно только поддерживать плодородность грунта мульчированием и внесением под перекопку навоза из расчета 3-4 кг/м². А выращиваемые в суглинке культуры следует регулярно подкармливать минеральными комплексами.'),
('Известковый', 'Известковые грунты могут быть тяжелыми или легкими, но все они бедные. Они включают много каменистых фрагментов, их pH сдвинут в щелочную сторону, они быстро нагреваются и высыхают, блокируют усвоение культурами марганца и железа, отчего у них желтеют листья и происходит задержка роста. Улучшить структуру грунта можно регулярным внесением органики под перекопку и использованием ее в виде мульчи, выращиванием и заделкой в верхний слой сидеральных культур, внесением калийных удобрений. После окультуривания в известковых грунтах можно выращивать любые культуры при условии своевременного полива, регулярных рыхлений междурядий и разумного внесения органических и минеральный удобрений.'),
('Торфяной', 'Торфяные, или болотистые грунты тоже нельзя назвать подходящими для земледелия, поскольку питательные элементы в них находятся в форме, недоступной для усвоения растениями. Эти грунты быстро впитывают и так же быстро отдают воду, медленно прогреваются и как правило закислены. Положительными качествами торфяной почвы можно считать то, что она подаются окультуриванию и задерживает в себе минеральные удобрения. Чтобы повысить плодородность торфяной почвы, ее глубоко перекапывают с глиняной мукой или песком, сильно закисленные участки известкуют, а в дальнейшем регулярно удобряют органикой – навозной жижей, компостом, перегноем, микробиологическими добавками и калийно-фосфорными удобрениями. При высаживании деревьев посадочные котлованы нужно заполнять специально составленной подходящей для культуры почвенной смесью, а при разбивке на торфяниках овощных грядок поступают так, как и с песчаным грунтом: укладывают в качестве основы глиняную прослойку, а поверх нее делают грядки из смеси торфа с суглинком, органическими удобрениями и известью.'),
('Черноземный', 'Чернозёмы – грунты высокой плодородности с устойчивой структурой, высоким содержанием гумуса и достаточным количеством кальция и других питательных элементов. Они хорошо поглощают и удерживают воздух, воду и тепло, поэтому для выращивания овощных, цветочных и плодово-ягодных культур являются лучшими из всех видов грунта. Но чернозём со временем истощается, и через 2-3 года непрерывного использования он требует внесения удобрений или восстановления структуры за счет выращивания сидератов. Нужно сказать, что чернозём не является легким грунтом, и под некоторые культуры его приходится перекапывать с торфом или песком. Кроме того, его реакция может быть как нейтральной, так и сдвинутой в щелочную или кислую сторону, поэтому чернозем может требовать как раскисления, так и расщелачивания.');


INSERT INTO connection_territories_soils (connection_territorie_id, connection_soil_id)
VALUES
(1, 1),
(2, 1),
(3, 2),
(3, 3),
(4, 2),
(4, 3),
(5, 2),
(5, 3);

INSERT INTO connection_soils_grounds (connection_soil_id, connection_ground_id)
VALUES
(1, 3),
(1, 4),
(2, 1),
(2, 2),
(2, 3),
(2, 4),
(3, 3),
(3, 4);

INSERT INTO connection_soils_plants (connection_soil_id, connection_plant_id, connection_soils_plants_isGood)
VALUES
(1, 1, TRUE),
(1, 4, TRUE),
(1, 5, TRUE),
(1, 6, FALSE),
(2, 1, TRUE),
(2, 2, TRUE),
(2, 3, TRUE),
(2, 4, TRUE),
(2, 5, TRUE),
(2, 6, TRUE),
(3, 1, TRUE),
(3, 2, TRUE),
(3, 4, TRUE),
(3, 5, TRUE),
(3, 6, FALSE);

INSERT INTO connection_plants_animals (connection_plant_id, connection_animal_id)
VALUES
(4, 1),
(4, 3),
(5, 1),
(5, 2);




 ''')

con.commit()

cursor = con.cursor()