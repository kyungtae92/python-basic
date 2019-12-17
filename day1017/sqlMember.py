sqlCreateDBInit = """insert into testdb.member1 (name, email, age)
             values (%s, %s, %s)"""
sqlMemberADD = """insert into testdb.member1 (name, email, age)
             values (%s, %s, %s)"""
sqlMemberAllList = "select name, email, age from testdb.member1 where name=%s"