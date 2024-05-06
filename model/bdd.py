def get_membresData():
cnx = connexion()
if cnx is None:
    return None

try:
    cursor = cnx.cursor(dictionary=True)
    sql = "SELECT * FROM identification"
    cursor.execute(sql)

    listeMembres = cursor.fetchall()

    close_bd(cursor, cnx)
    
#session['successDB'] = "OK get_membresData"
except mysql.connector.Error as err:

listeMembres = None

session['errorDB'] = "Failed get membres data : {}".format(err)

return listeMembres