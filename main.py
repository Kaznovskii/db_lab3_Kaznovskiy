import psycopg2
import matplotlib.pyplot as plt

username = 'AntonK_KM_02'
password = '2222'
database = 'db_lab2_Kaznovskyi'
host = 'localhost'
port = '5432'

query_1 = '''
DROP VIEW IF EXISTS Qua_of_CertType;
CREATE VIEW Qua_of_CertType AS
SELECT TRIM(certifications.certification_name) AS certificate_type, COUNT(courses.certification_id) 
FROM courses 
JOIN certifications ON certifications.certification_id = courses.certification_id
GROUP BY certification_name;
SELECT * FROM Qua_of_CertType;
'''

query_2 = '''
DROP VIEW IF EXISTS Diff_Levels;
CREATE VIEW Diff_Levels AS
SELECT TRIM(difficulty.difficulty_level) AS difficulty, COUNT(courses.difficulty_id) FROM courses 
JOIN difficulty ON difficulty.difficulty_id = courses.difficulty_id
GROUP BY difficulty_level
ORDER BY COUNT(courses.difficulty_id);
SELECT * FROM Diff_Levels;
'''

query_3 = '''
DROP VIEW IF EXISTS Show_Lower_Students;
CREATE VIEW Show_Lower_Students AS
SELECT TRIM(course_title) AS course_title, amount_of_students AS amount_of_students_k  FROM courses
WHERE amount_of_students < 100.0
ORDER BY amount_of_students;
SELECT * FROM Show_Lower_Students;
'''

conn = psycopg2.connect(user=username, password=password, dbname=database, host=host, port=port)


with conn:
    cur = conn.cursor()

# query_1
    cur.execute(query_1)
    types = []
    n_courses = []

    for row in cur:
        types.append(row[0])
        n_courses.append(row[1])

    x_range = range(len(types))

    figure, (bar_ax, pie_ax, graph_ax) = plt.subplots(1, 3)

    bar_ax.bar(x_range, n_courses, label='Total')
    bar_ax.set_title('Quantity of each type of cert')
    bar_ax.set_xlabel('Courses')
    bar_ax.set_ylabel('Amount of wines')
    bar_ax.set_xticks(x_range)
    bar_ax.set_xticklabels(types, rotation=45)

# query_2
    cur.execute(query_2)
    difficult_lvl = []
    courses = []

    for row in cur:
        difficult_lvl.append(row[0])
        courses.append(row[1])

    pie_ax.pie(courses, labels=difficult_lvl, autopct='%1.1f%%')
    pie_ax.set_title('Difficult levels')

# query_3
    cur.execute(query_3)
    title = []
    quantity = []

    for row in cur:
        title.append(row[0])
        quantity.append(row[1])

    graph_ax.plot(title, quantity, marker='o')
    graph_ax.set_xlabel('Courses')
    graph_ax.set_ylabel('Quantity of student`s (k)')
    graph_ax.set_title('Courses where quantity of student`s less than 100.000')
    graph_ax.set_xticklabels(title, rotation=40)

    for qnt, price in zip(title, quantity):
        graph_ax.annotate(price, xy=(qnt, price), xytext=(7, 2), textcoords='offset points')


mng = plt.get_current_fig_manager()
mng.resize(1400, 750)

plt.subplots_adjust(left=0.1, bottom=0.19, right=0.94, top=0.9, wspace=0.4, hspace=0.4)

plt.show()
