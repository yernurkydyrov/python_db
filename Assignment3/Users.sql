CREATE TABLE public.users (
	"id" integer primary key NOT NULL,
    login text not NULL,
	"password" text not NULL,
	"token" text NULL
);

INSERT INTO public.users ("id",login,"password") values (1,'admin','password'), (2,'user1','password'), (3,'user2','password')



