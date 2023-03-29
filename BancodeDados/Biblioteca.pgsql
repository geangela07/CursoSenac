--
-- PostgreSQL database dump
--

-- Dumped from database version 15.1
-- Dumped by pg_dump version 15.1

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: Aluguel; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public."Aluguel" (
    "ID" integer NOT NULL,
    "ID_Cliente" integer NOT NULL,
    "ID_Livro" integer NOT NULL,
    "Data_Aluguel" timestamp without time zone DEFAULT CURRENT_TIMESTAMP
);


ALTER TABLE public."Aluguel" OWNER TO postgres;

--
-- Name: Aluguel_ID_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

ALTER TABLE public."Aluguel" ALTER COLUMN "ID" ADD GENERATED ALWAYS AS IDENTITY (
    SEQUENCE NAME public."Aluguel_ID_seq"
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);


--
-- Name: Cliente; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public."Cliente" (
    "ID" integer NOT NULL,
    "Nome" character varying(255) NOT NULL,
    "CPF" character(11) NOT NULL
);


ALTER TABLE public."Cliente" OWNER TO postgres;

--
-- Name: Cliente_ID_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

ALTER TABLE public."Cliente" ALTER COLUMN "ID" ADD GENERATED ALWAYS AS IDENTITY (
    SEQUENCE NAME public."Cliente_ID_seq"
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);


--
-- Name: Livro; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public."Livro" (
    "ID" integer NOT NULL,
    "Nome" character varying(255) NOT NULL,
    "Autor" character varying(255) NOT NULL
);


ALTER TABLE public."Livro" OWNER TO postgres;

--
-- Name: Livro_ID_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

ALTER TABLE public."Livro" ALTER COLUMN "ID" ADD GENERATED ALWAYS AS IDENTITY (
    SEQUENCE NAME public."Livro_ID_seq"
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);


--
-- Name: Livros; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public."Livros" (
    "ID" integer NOT NULL,
    "Nome" character varying(255) NOT NULL,
    "Paginas" numeric NOT NULL,
    "AnoLançamento" numeric NOT NULL,
    "Autor" character varying(255) NOT NULL
);


ALTER TABLE public."Livros" OWNER TO postgres;

--
-- Name: Livros_ID_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public."Livros_ID_seq"
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public."Livros_ID_seq" OWNER TO postgres;

--
-- Name: Livros_ID_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public."Livros_ID_seq" OWNED BY public."Livros"."ID";


--
-- Name: Livros ID; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."Livros" ALTER COLUMN "ID" SET DEFAULT nextval('public."Livros_ID_seq"'::regclass);


--
-- Data for Name: Aluguel; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public."Aluguel" ("ID", "ID_Cliente", "ID_Livro", "Data_Aluguel") FROM stdin;
\.


--
-- Data for Name: Cliente; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public."Cliente" ("ID", "Nome", "CPF") FROM stdin;
\.


--
-- Data for Name: Livro; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public."Livro" ("ID", "Nome", "Autor") FROM stdin;
\.


--
-- Data for Name: Livros; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public."Livros" ("ID", "Nome", "Paginas", "AnoLançamento", "Autor") FROM stdin;
\.


--
-- Name: Aluguel_ID_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public."Aluguel_ID_seq"', 1, false);


--
-- Name: Cliente_ID_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public."Cliente_ID_seq"', 1, false);


--
-- Name: Livro_ID_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public."Livro_ID_seq"', 1, false);


--
-- Name: Livros_ID_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public."Livros_ID_seq"', 1, false);


--
-- Name: Aluguel Aluguel_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."Aluguel"
    ADD CONSTRAINT "Aluguel_pkey" PRIMARY KEY ("ID");


--
-- Name: Cliente Cliente_CPF_key; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."Cliente"
    ADD CONSTRAINT "Cliente_CPF_key" UNIQUE ("CPF");


--
-- Name: Cliente Cliente_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."Cliente"
    ADD CONSTRAINT "Cliente_pkey" PRIMARY KEY ("ID");


--
-- Name: Livro Livro_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."Livro"
    ADD CONSTRAINT "Livro_pkey" PRIMARY KEY ("ID");


--
-- Name: Livros Livros_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."Livros"
    ADD CONSTRAINT "Livros_pkey" PRIMARY KEY ("ID");


--
-- Name: Aluguel fk_cliente; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."Aluguel"
    ADD CONSTRAINT fk_cliente FOREIGN KEY ("ID_Cliente") REFERENCES public."Cliente"("ID") ON DELETE CASCADE;


--
-- Name: Aluguel fk_livro; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."Aluguel"
    ADD CONSTRAINT fk_livro FOREIGN KEY ("ID_Livro") REFERENCES public."Livro"("ID") ON DELETE SET NULL;


--
-- PostgreSQL database dump complete
--

