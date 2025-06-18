from flet_core import row

from database.DB_connect import DBConnect
from model.collegamento import Collegamento
from model.stato import Stato

class DAO():

    @staticmethod
    def getAllNodes(year):
        conn = DBConnect.get_connection()
        cursor = conn.cursor(dictionary=True)

        result = []

        query = """ SELECT c.state1no, c.state1ab
                    FROM contiguity c 
                    WHERE c.year <= %s
                    and c.conttype = 1
                    GROUP BY c.state1no, c.state1ab
                """
        cursor.execute(query,(year,))

        for row in cursor:
            result.append( Stato(row['state1no'], row['state1ab']) )

        cursor.close()
        conn.close()

        return result



    @staticmethod
    def getAllEdges(year):
        conn = DBConnect.get_connection()
        cursor = conn.cursor(dictionary=True)

        result = []

        query = """ SELECT c.state1no, c.state1ab, c.state2no, c.state2ab
                    FROM contiguity c 
                    WHERE c.year <= %s and c.conttype = 1
                    """
        cursor.execute(query,(year,))

        for row in cursor:
            result.append( Collegamento( Stato( row['state1no'], row['state1ab'] ), Stato( row['state2no'], row['state2ab'] ) ) )

        cursor.close()
        conn.close()

        return result

    @staticmethod
    def getConfinanti(year):
        conn = DBConnect.get_connection()
        cursor = conn.cursor(dictionary=True)

        result = []

        query = """ SELECT c.state1no, COUNT(*) as nConf
                    FROM contiguity c 
                    WHERE year <= %s and c.conttype = 1
                    GROUP BY c.state1no
                """
        cursor.execute(query, (year, ))

        for row in cursor:
            result.append( (row['state1no'], row['nConf']) )

        cursor.close()
        conn.close()

        return result