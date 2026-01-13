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
        subject_id=int(input("enter subject id"))
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
        '''
        val=(subject_id,)
        table=pd.read_sql(query,self.conn,params=val)
        print(table)
       
analysis=Performance_Analytics(conn,cursor)
