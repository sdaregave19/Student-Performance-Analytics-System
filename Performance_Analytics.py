from database_connection import get_connection
# import _mysql_connector
import pandas as pd
import matplotlib.pyplot as plt
def load_connection():
    conn=get_connection()
    cursor=conn.cursor()
    return conn,cursor

conn,cursor=load_connection()

class Performance_Analytics:
    
    def __init__(self,conn,cursor):
        self.conn=conn
        self.cursor=cursor
    
    def Subject_wise_Average_Marks(self):
        query = '''
            SELECT s.subject_name,
                   AVG(m.marks) AS avg_marks
            FROM marks AS m
            INNER JOIN subjects AS s ON s.subject_id = m.subject_id
            GROUP BY s.subject_name
            ORDER BY avg_marks DESC;
        '''
        query1=self.cursor.execute(query)
        rows=self.cursor.fetchall()
        # 3️⃣ Read SQL into Pandas DataFrame
        # table = pd.read_sql(query1, self.conn)
        table=pd.DataFrame(rows,columns=[x[0] for x in self.cursor.description])
        print(table)
        # 4️⃣ Close connection
        self.conn.close()
        
        # 5️⃣ Plot
    
        plt.figure(figsize=(8,5))
        plt.bar(table['subject_name'],table['avg_marks'],color='red')
        plt.xlabel("Subject")
        plt.ylabel("Average Marks")
        plt.title("Subject-wise Average Marks")
        plt.ylim(0, 100)
        plt.savefig("Subject_wise_Average_Marks")
    
    def Top3persubject (self):
        subject_id=int(input("enter subject id -> "))
        query='''SELECT
                    st.name,
                    m.student_id,
                    m.subject_id,
                    m.marks
                FROM subjects AS s
                INNER JOIN marks AS m ON s.subject_id=m.subject_id
                INNER JOIN students AS st ON st.student_id=m.student_id
                WHERE m.subject_id=%s
                ORDER BY m.marks DESC
                LIMIT 3
        '''
        val=(subject_id,)
        table=pd.read_sql(query,self.conn,params=val)
        print(table)
        
        query2=self.cursor.execute(query,val)
        rows=self.cursor.fetchall()
        df=pd.DataFrame(rows,columns=[x[0] for x in self.cursor.description])
        
        self.conn.close()
        
        plt.figure(figsize=(5,5))
        plt.plot(df['name'],df['marks'],marker='o',color='red')
        plt.xlabel("NAME")
        plt.ylabel("Marks")
        plt.title("Top3persubject")
        plt.ylim(0, 100)
        plt.savefig("op3persubject")
        
    def At_risk_students_list(self):
        query='''SELECT 
                    st.name,
                    a.student_id,
                    a.attendance_percentage,
                    AVG(m.marks) AS avg_marks
                FROM marks AS m
                INNER JOIN attendance AS a ON m.student_id=a.student_id
                INNER JOIN students AS st ON st.student_id=m.student_id
                WHERE a.attendance_percentage <80 
                GROUP BY st.name,
                    a.student_id,
                    a.attendance_percentage
                HAVING avg_marks<70
                ORDER BY a.student_id DESC
        '''
        table=pd.read_sql(query,self.conn)
        print(table)
        
        # query2=self.cursor.execute(query)
        # rows=self.cursor.fetchall()
        # df=pd.DataFrame(rows,columns=[x[0] for x in self.cursor.description])
        
        # self.conn.close()
        
analysis=Performance_Analytics(conn,cursor)
