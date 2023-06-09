# VRK_Barchelor_LandscapeDesign

СЕРВЕРНАЯ ЧАСТЬ. Выполнил: студент группы Б9119-02.03.03техпро Л. И. Болычев

Научный руководитель: профессор департамента ПИиИИ, д.т.н., профессор И. Л. Артемьева

Клиентскую часть работы выполнил Н. О. Румянцев (https://github.com/Hostridet/SoilVKR), работа целиком также находится у него, здесь только серверная часть.

Используется сервер Uvicorn.

## Использование   
```SWAGGER(просмотр запросов): (http://127.0.0.1:8000/docs)```  
------------------------------------------------------------------------------------------

<details>
    <summary>Таблицы</summary> <!-- Good place for a CTA (Call to Action) -->
 <!-- empty line *️⃣  -->
    ------------------------------------------------------------------------------------------

**users - таблица пользователей**  



user_id AUTOINCREMENT,  
user_login NOT NULL,  
user_password NOT NULL, - пароль 
user_FIO NOT NULL,  
user_email NOT NULL,  
user_isAdmin NOT NULL - является ли пользователь админом  

------------------------------------------------------------------------------------------

**territories - таблица территорий (то есть точек земной поверхности)**  


  
territorie_id AUTOINCREMENT,  
territorie_coord_x NOT NULL, - широта территории  
territorie_coord_y NOT NULL, - долгота территории  
territorie_address NOT NULL - адрес территории (строка с описанием места)

------------------------------------------------------------------------------------------

**soils**  


  
soil_id AUTOINCREMENT,  
soil_name NOT NULL,  
soil_description NOT NULL, - текстовое описание почвы  
soil_acidity, - кислотность почвы
soil_minerals, - минералы в почве 
soil_profile - профиль почвы  

------------------------------------------------------------------------------------------

**grounds**  


  
ground_id AUTOINCREMENT,  
ground_name NOT NULL,  
ground_description NOT NULL, - текстовое описание грунта  
ground_density, - твёрдость грунта
ground_humidity, - влажность грунта
ground_hardness_Moos - жёсткость грунта по шкале Мооса

------------------------------------------------------------------------------------------

**plants**  


  
plant_id AUTOINCREMENT,  
plant_name NOT NULL,  
plant_description NOT NULL, - текстовое описание растения  
plant_isFodder NOT NULL, - является ли растение кормовым (подходит ли для откорма скота)  
plant_isManyYears, - является ли растение многолетним  
plant_isTwoYears, - является ли растение двулетним  
plant_isOneYear, - является ли растение однолетним (ВАЖНО: это разные параметры; бывают растения, которые одновременно однолетние и многолетние, например)  
plant_isExactingToTheLight, - требовательно ли к свету растение  
plant_climat, - краткое описание подходящего для растения климата  
plant_required_minerals_and_trace_elements, - требуемые для растения минералы и микроэлементы
plant_temperature_min, - минимальная температура для роста растения  
plant_temperature_max, - максимальная температура для роста растения  
plant_kingdom, - царство ("Растения" или "Грибы")  
plant_philum, - тип (отдел)  
plant_class, - класс  
plant_order, - порядок  
plant_family, - семейство  
plant_genus, - род  
plant_species - вид  

------------------------------------------------------------------------------------------

**animals**  


  
animal_id AUTOINCREMENT,  
animal_name NOT NULL,  
animal_description NOT NULL, - текстовое описание животного  
animal_kingdom, - царство (всегда "Животные")  
animal_philum, - тип (отдел)  
animal_class, - класс  
animal_order, - порядок  
animal_family, - семейство  
animal_genus, - род  
animal_species - вид  

------------------------------------------------------------------------------------------

**connection_connection_territories_soils - таблица-связка для территорий и почв (в какой точке земной поверхности какая почва)**  


  
connection_territories_soils_id AUTOINCREMENT,  
connection_territorie_id NOT NULL,  
connection_soil_id NOT NULL  

------------------------------------------------------------------------------------------

**connection_soils_grounds - таблица-связка для почв и грунтов (для каких почв характерны какие грунты)**  


  
connection_soils_grounds_id AUTOINCREMENT,  
connection_soil_id NOT NULL,  
connection_ground_id NOT NULL  

------------------------------------------------------------------------------------------

**connection_soils_plants - таблица-связка для почв и растений (на какой почве как растут какие растения)**  


  
connection_soils_plants_id AUTOINCREMENT,  
connection_soil_id NOT NULL,  
connection_plant_id NOT NULL

------------------------------------------------------------------------------------------

**connection_plants_animals - таблица-связка для растений и животных (какие животные питаются какими растениями)**  


  
connection_plants_animals_id AUTOINCREMENT,  
connection_plant_id NOT NULL,  
connection_animal_id NOT NULL  

------------------------------------------------------------------------------------------
</details>
