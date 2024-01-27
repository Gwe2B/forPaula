# Installation du projet
Prérequis :
 - Python installé sur la machine (lol)

Pense à installer les dépendances en tapant dans un CMD :
```
pip install -r requirements.txt
--- OR ---
python -m pip install -r requirements.txt
```
(evideament il faut que le CMD soit ouvert dans le dossier du projet, si tu a des difficultés dit le moi)

# Requêtes HTTP(S)

Une requete se compose de 3 parties :
 - l'URL : le fameu http(s)://azerty.fr/ que tu compléte d'une méthode HTTP (cf. plus bas)
 - l'en-tête (Header) : va décrire la requete et contient tout un tas d'informations afin que le seveur et toi puissent communiqué et vous comprendre.
 - le corps (body) : qui contient les données que tu désire transmettre au seveur.

## L'URL

Une URL peut être décomposer en plusieurs parties.

Prenons l'URL suivante : `https://mail.google.com/mail/u/0/?subject=Lorem&author=toto@gmail.com` (elle est inventé)

On peut la découper comme suit :
 - `https`: Le protocole internet utilisé. Il en existe pleins mais ceux que tu doit absoluments connaitres sont :
    - `http` : Hyper Text Transfer Protocol => Permet de naviguer sur le WEB
    - `https` : Hyper Text Transfer Protocol Secure => Idem mais les communications sont crypter entre toi et le serveur. En **théorie** personne ne peut plus "écouter aux portes".
 - `mail.` : C'est ce qu'on appel un sous-domaine.
 - `google.com` : C'est le domaine (plus exactement le nom de domaine, afin de pas avoir à taper des adresses IP)
 - `/mail/u/0/` : C'est ce qu'on appel l'endpoint. C'est l'adresse de la ressources que tu demande.
 - `?subject=Lorem&author=toto@gmail.com` : C'est ce que l'on appel une "query string". C'est une chaine de caractere qui contient des informations utile lors d'une requete http. Ici en locurence on à deux "query params" qui sont `subject` (qui vaut "Lorem Ipsum") et `author` (qui vaut "toto@gmail.com").

### Méthodes HTTP
Il en existe 5 standard qui suivent une norme (du moins quand l'API/projet n'est pas dev avec le cul) :
 - GET : Pour récupérer une ressource ou une liste de ressource
 - POST : Pour créer/ajouter une ressource
 - PATCH : Pour "remplacer" une ressource (on parle aussi de mise à jour complète)
 - PUT : Pour mettre une ressource à jour (on parle aussi de mise à jour partiel)
 - DELETE : Pour supprimer une ressource

Les méthodes POST, PUT et PATCH attendent souvent ce qu'on appel un corps de
requête (body). C'est à dire des données décrivant la ressource. Le format
utilisé pour les ressources est souvent du JSON bien que l'on trouve également
du YAML et du XML (ce sont des formalismes, si tu ne connais pas je t'encourage
à te renseigner).

## En-tête
Je ne citerais ici que les champs importants du Header. Il en existe tout un tas
que je t'invite à regarder.

 - Accept : Définit le type MIME de la réponse que **TU** attend de la part du serveur.
 - Content-Type : Définit le type MIME du contenue de la requête.
 - Authorization : Permet de transporter des informations d'authentification tel
 que des clés d'API (pas dans notre cas), des tokens d'authentifications, etc...

Tu trouvera une liste exhaustive des différents en-tête sur la doc [MDN](https://developer.mozilla.org/fr/docs/Web/HTTP/Headers)

Concernant les types MIME il s'agit d'une manière de décrire le type d'une données
un peu comme les extensions de fichiers. Pour plus d'infos la doc [MDN](https://developer.mozilla.org/fr/docs/Web/HTTP/Basics_of_HTTP/MIME_types/Common_types) est ton ami. 

## Réponses aux requêtes
Les réponses, en plus des infos précédantes, sont caractérisé par un code HTTP
sur trois chiffres que l'on appel aussi "status" ou "status code". Il en existe
encore une fois un paquet donc je ne vérrais ici que les principaux.

### 1XX
Les codes HTTP compris entre 100 et 199 inclus sont des réponses informatives.
Je rentrerais pas dans le détails persos j'en ai jamais vue.

### 2XX
Les codes HTTP compris entre 200 et 299 inclus sont des succés.
 - "200 : Success" -> La requete à réussi
 - "201 : Created" -> Informe que la ressource est crée.
 - "204 : No Content" -> La requete à réussi mais aucune infos n'est retourné. C'est souvent le cas des requêtes DELETE

### 3XX
Les codes HTTP compris entre 300 et 399 inclus sont des réponses de redirection.
Je rentrerais pas dans le détails ce sont des réponses assez peu fréquentes sur des API.

### 4XX
Les codes HTTP compris entre 400 et 499 inclus informe d'une erreur de la part du client. Donc de **TA** part (ou de celle de ton utilisateur).
 - "400 : Bad Request" -> Le serveur n'a pas compris ce que tu voulais. Le corps de la réponse n'est pas celui qu'il attend par exemple.
 - "401 : Unhauthorized" -> Le client n'est pas authentifier (et doit le faire)
 - "403 : Forbidden" -> Accés interdit
 - "404 : Not Found" -> Je pense que tu le connais, le serveur ne trouve pas ce que tu demande.
 - "418 : I am a teapot" -> Le serveur refuse de brasser du café avec une théière.

Bon d'accord le 418 n'a aucun interet et tu le croisera jamais. Mais moi il me fait toujours autant rire.

### 5XX
Les codes HTTP compris entre 500 et 599 inclus informe d'une erreur de la part du sevreur. Donc de la part de l'API.
 - "500 : Internal server error" -> Le serveur à rencontré une erreur qu'il n'arrive pas à gérer.

Pour plus d'infos encore une fois la doc [MDN](https://developer.mozilla.org/fr/docs/Web/HTTP/Status)

Je pense qu'on à fait plus ou moins le tour. Au cas ou tu l'est pas compris la doc MDN est un peu la bible en matière de WEB.
