PGDMP     5                     {            BibliotecaNova    15.1    15.1                0    0    ENCODING    ENCODING        SET client_encoding = 'UTF8';
                      false                       0    0 
   STDSTRINGS 
   STDSTRINGS     (   SET standard_conforming_strings = 'on';
                      false                       0    0 
   SEARCHPATH 
   SEARCHPATH     8   SELECT pg_catalog.set_config('search_path', '', false);
                      false                       1262    32870    BibliotecaNova    DATABASE     �   CREATE DATABASE "BibliotecaNova" WITH TEMPLATE = template0 ENCODING = 'UTF8' LOCALE_PROVIDER = libc LOCALE = 'Portuguese_Brazil.1252';
     DROP DATABASE "BibliotecaNova";
                postgres    false            �            1259    32871    Aluguel    TABLE     �   CREATE TABLE public."Aluguel" (
    "ID" integer NOT NULL,
    "ID_Cliente" integer NOT NULL,
    "ID_Livro" integer NOT NULL,
    "Data_Aluguel" timestamp without time zone DEFAULT CURRENT_TIMESTAMP
);
    DROP TABLE public."Aluguel";
       public         heap    postgres    false            �            1259    32875    Aluguel_ID_seq    SEQUENCE     �   ALTER TABLE public."Aluguel" ALTER COLUMN "ID" ADD GENERATED ALWAYS AS IDENTITY (
    SEQUENCE NAME public."Aluguel_ID_seq"
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);
            public          postgres    false    214            �            1259    32876    Cliente    TABLE     �   CREATE TABLE public."Cliente" (
    "ID" integer NOT NULL,
    "Nome" character varying(255) NOT NULL,
    "CPF" character(11) NOT NULL
);
    DROP TABLE public."Cliente";
       public         heap    postgres    false            �            1259    32879    Cliente_ID_seq    SEQUENCE     �   ALTER TABLE public."Cliente" ALTER COLUMN "ID" ADD GENERATED ALWAYS AS IDENTITY (
    SEQUENCE NAME public."Cliente_ID_seq"
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);
            public          postgres    false    216            �            1259    32880    Livro    TABLE     �   CREATE TABLE public."Livro" (
    "ID" integer NOT NULL,
    "Nome" character varying(255) NOT NULL,
    "Autor" character varying(255) NOT NULL
);
    DROP TABLE public."Livro";
       public         heap    postgres    false            �            1259    32885    Livro_ID_seq    SEQUENCE     �   ALTER TABLE public."Livro" ALTER COLUMN "ID" ADD GENERATED ALWAYS AS IDENTITY (
    SEQUENCE NAME public."Livro_ID_seq"
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);
            public          postgres    false    218            �            1259    32886    Livros    TABLE     �   CREATE TABLE public."Livros" (
    "ID" integer NOT NULL,
    "Nome" character varying(255) NOT NULL,
    "Paginas" numeric NOT NULL,
    "AnoLançamento" numeric NOT NULL,
    "Autor" character varying(255) NOT NULL
);
    DROP TABLE public."Livros";
       public         heap    postgres    false            �            1259    32891    Livros_ID_seq    SEQUENCE     �   CREATE SEQUENCE public."Livros_ID_seq"
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 &   DROP SEQUENCE public."Livros_ID_seq";
       public          postgres    false    220                       0    0    Livros_ID_seq    SEQUENCE OWNED BY     E   ALTER SEQUENCE public."Livros_ID_seq" OWNED BY public."Livros"."ID";
          public          postgres    false    221            u           2604    32892 	   Livros ID    DEFAULT     l   ALTER TABLE ONLY public."Livros" ALTER COLUMN "ID" SET DEFAULT nextval('public."Livros_ID_seq"'::regclass);
 <   ALTER TABLE public."Livros" ALTER COLUMN "ID" DROP DEFAULT;
       public          postgres    false    221    220                      0    32871    Aluguel 
   TABLE DATA           S   COPY public."Aluguel" ("ID", "ID_Cliente", "ID_Livro", "Data_Aluguel") FROM stdin;
    public          postgres    false    214   z                 0    32876    Cliente 
   TABLE DATA           8   COPY public."Cliente" ("ID", "Nome", "CPF") FROM stdin;
    public          postgres    false    216   �                 0    32880    Livro 
   TABLE DATA           8   COPY public."Livro" ("ID", "Nome", "Autor") FROM stdin;
    public          postgres    false    218   �                 0    32886    Livros 
   TABLE DATA           V   COPY public."Livros" ("ID", "Nome", "Paginas", "AnoLançamento", "Autor") FROM stdin;
    public          postgres    false    220   0                   0    0    Aluguel_ID_seq    SEQUENCE SET     >   SELECT pg_catalog.setval('public."Aluguel_ID_seq"', 1, true);
          public          postgres    false    215                        0    0    Cliente_ID_seq    SEQUENCE SET     >   SELECT pg_catalog.setval('public."Cliente_ID_seq"', 1, true);
          public          postgres    false    217            !           0    0    Livro_ID_seq    SEQUENCE SET     <   SELECT pg_catalog.setval('public."Livro_ID_seq"', 1, true);
          public          postgres    false    219            "           0    0    Livros_ID_seq    SEQUENCE SET     >   SELECT pg_catalog.setval('public."Livros_ID_seq"', 1, false);
          public          postgres    false    221            w           2606    32894    Aluguel Aluguel_pkey 
   CONSTRAINT     X   ALTER TABLE ONLY public."Aluguel"
    ADD CONSTRAINT "Aluguel_pkey" PRIMARY KEY ("ID");
 B   ALTER TABLE ONLY public."Aluguel" DROP CONSTRAINT "Aluguel_pkey";
       public            postgres    false    214            y           2606    32896    Cliente Cliente_CPF_key 
   CONSTRAINT     W   ALTER TABLE ONLY public."Cliente"
    ADD CONSTRAINT "Cliente_CPF_key" UNIQUE ("CPF");
 E   ALTER TABLE ONLY public."Cliente" DROP CONSTRAINT "Cliente_CPF_key";
       public            postgres    false    216            {           2606    32898    Cliente Cliente_pkey 
   CONSTRAINT     X   ALTER TABLE ONLY public."Cliente"
    ADD CONSTRAINT "Cliente_pkey" PRIMARY KEY ("ID");
 B   ALTER TABLE ONLY public."Cliente" DROP CONSTRAINT "Cliente_pkey";
       public            postgres    false    216            }           2606    32900    Livro Livro_pkey 
   CONSTRAINT     T   ALTER TABLE ONLY public."Livro"
    ADD CONSTRAINT "Livro_pkey" PRIMARY KEY ("ID");
 >   ALTER TABLE ONLY public."Livro" DROP CONSTRAINT "Livro_pkey";
       public            postgres    false    218                       2606    32902    Livros Livros_pkey 
   CONSTRAINT     V   ALTER TABLE ONLY public."Livros"
    ADD CONSTRAINT "Livros_pkey" PRIMARY KEY ("ID");
 @   ALTER TABLE ONLY public."Livros" DROP CONSTRAINT "Livros_pkey";
       public            postgres    false    220            �           2606    32903    Aluguel fk_cliente    FK CONSTRAINT     �   ALTER TABLE ONLY public."Aluguel"
    ADD CONSTRAINT fk_cliente FOREIGN KEY ("ID_Cliente") REFERENCES public."Cliente"("ID") ON DELETE CASCADE;
 >   ALTER TABLE ONLY public."Aluguel" DROP CONSTRAINT fk_cliente;
       public          postgres    false    214    216    3195            �           2606    32908    Aluguel fk_livro    FK CONSTRAINT     �   ALTER TABLE ONLY public."Aluguel"
    ADD CONSTRAINT fk_livro FOREIGN KEY ("ID_Livro") REFERENCES public."Livro"("ID") ON DELETE SET NULL;
 <   ALTER TABLE ONLY public."Aluguel" DROP CONSTRAINT fk_livro;
       public          postgres    false    218    214    3197               ,   x�3�4B##c]#]#sCC+#S+#C=#ScsC3�=... }Xs            x�3�t�K�0�4364172V������ 8�3         ;   x�3�t��LNU��W(H<��X!%�X!7�(�,3'#���'�<�X�9��(?'�+F��� �C8            x������ � �     