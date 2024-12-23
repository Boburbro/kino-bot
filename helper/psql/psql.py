from helper.psql.base_psql import check_func
from helper.psql.psql_asks import PSQLAsks
from helper.psql.psql_channels import PSQLChannel


class PSQL(PSQLChannel, PSQLAsks):
    @check_func
    def initDataBase(self):
        self.cur.execute(
            """
    CREATE TABLE IF NOT EXISTS asks (
        channel_id BIGINT, user_id BIGINT
    );
    CREATE TABLE IF NOT EXISTS channels (
        id BIGINT PRIMARY KEY, 
        title TEXT, 
        link TEXT, 
        plan BIGINT
    );

    CREATE TABLE IF NOT EXISTS movies (
        id BIGINT PRIMARY KEY,
        video_id TEXT, 
        caption TEXT,
        download_count TEXT
    );
            """
        )

        self.conn.commit()

        # self.cur.execute(
        #     """
        #     CREATE OR REPLACE FUNCTION update_updated_at_column_users()
        #     RETURNS TRIGGER AS $$
        #     BEGIN
        #         NEW.updated_at = CURRENT_TIMESTAMP;
        #         RETURN NEW;
        #     END;
        #     $$ LANGUAGE plpgsql;
        # """
        # )

        # self.cur.execute(
        #     """
        #     CREATE TRIGGER set_updated_at_users
        #     BEFORE UPDATE ON users
        #     FOR EACH ROW
        #     EXECUTE FUNCTION update_updated_at_column_users();
        # """
        # )
