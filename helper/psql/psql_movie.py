from data.models.movie_model import MovieModel
from helper.psql.base_psql import BasePSQL, check_func


class PSQLMovie(BasePSQL):

    @check_func
    async def getMovies(self):
        print(f"{__file__} is running")
        self.cur.execute("SELECT * FROM movies;")
        rows = self.cur.fetchall()
        return [MovieModel.fromJson(row) for row in rows]

    @check_func
    async def getMovieById(self, id: int):
        print(f"{__file__} is running")
        self.cur.execute("SELECT * FROM movies WHERE id=%s", (id,))
        row = self.cur.fetchone()
        if row:
            return MovieModel.fromJson(row)
        else:
            return None

    @check_func
    async def createMovie(self, movie: MovieModel):
        print(f"{__file__} is running")
        try:
            query = """
            INSERT INTO movies (
              id, 
              video_id, 
              caption, 
              download_count, 
            ) VALUES (%s, %s, %s, %s);"""
            self.cur.execute(
                query,
                (
                    movie.id,
                    movie.video_id,
                    movie.caption,
                    movie.download_count,
                ),
            )
        except Exception as e:
            print(f"Error creating movie: {e}")
            self.conn.commit()
            return False

        self.conn.commit()
        return True

    @check_func
    async def updateMovie(self, movie: MovieModel):
        print(f"{__file__} is running")
        try:
            query = """
            UPDATE movies 
            SET video_id=%s, caption=%s, download_count=%s 
            WHERE id=%s;"""
            self.cur.execute(
                query,
                (
                    movie.video_id,
                    movie.caption,
                    movie.download_count,
                    movie.id,
                ),
            )
        except Exception as e:
            print(f"Error updating movie: {e}")
            self.conn.commit()
            return False

        self.conn.commit()
        return True

    @check_func
    async def deleteMovie(self, id: int):
        print(f"{__file__} is running")
        self.cur.execute("DELETE FROM movies WHERE id=%s;", (id,))
        self.conn.commit()
        return True
