# -*- coding: UTF-8 -*-
class Posts(object):

    def __init__(self, connection):
        self._connection = connection
    
    ##
    # retorna todas as postagens
    ##
    def selectall(self):
        cur = self._connection.execute("SELECT * FROM posts")
        entries = cur.fetchall()
        data = []

        for row in entries:
            d = dict(zip(row.keys(), row)) 
            data.append(d)

        return data

    ##
    # Retorna a postagem informada pelo ID
    ##
    def selectmessage(self, id):
        query = "SELECT * FROM posts WHERE id = %s" % id
        cur = self._connection.execute(query)
        entries = cur.fetchall()

        data = []

        for row in entries:
            d = dict(zip(row.keys(), row)) 
            data.append(d)

        return data

    ##
    # Retorna todas as mensagens do usuário
    ##
    def selectmessagesfromuser(user):
        query = "SELECT * FROM posts WHERE user = '%s'" % user
        cur = self._connection.execute(query)
        entries = cur.fetchall()

        data = []

        for row in entries:
            d = dict(zip(row.keys(), row)) 
            data.append(d)

        return data
    
    ##
    # Insere um novo post
    ##
    def insert(self, user=None, message=None):
        query = "INSERT INTO posts ('user', 'message') VALUES('%s', '%s');" % (user, message)
        cur = self._connection.cursor()
        cur.execute(query)
        res = self._connection.commit()

        #Novo Record
        id = cur.lastrowid
        newRecord = self.selectmessage(id)
        return newRecord[0]

    def update(self, id, user=None, message=None):
        pass
    
    ##
    # Deleta um post
    ##
    def delete(self, id):
        query = "DELETE FROM posts WHERE id = %i" % id
        cur = self._connection.cursor()
        cur.execute(query)
        return self._connection.commit()