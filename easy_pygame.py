import pygame

def init(display_size:tuple|None=None, window_title:str|None=None):
    """
    Inicia o epygame.

    ***display_size*** é o valor do tamanho da janela.
    
    ***window_title*** é o nome da janela.
    """
    pygame.init();
    global screen
    if display_size is None:
        screen = pygame.display.set_mode((1080,720));
    else:
        screen = pygame.display.set_mode(display_size);
    if window_title is None:
        pygame.display.set_caption("easy_pygame window");
    else:
        pygame.display.set_caption(window_title);
    global clock 
    clock = pygame.time.Clock();
    global dt
    dt = 0;
    global key_status
    key_status = {};

def get_events():
    global events
    events = [];
    for event in pygame.event.get():
        events.append(event);
    return events;

def isquiting():
    """
    Retorna verdadeiro quando o aplicativo estiver sendo fechado.

    Normalmente se utiliza assim:
    ```
    if isquiting():
        quit(); # Fechar Programa.
    ```
    """
    _bool = False;
    for event in events:
        if event.type == pygame.QUIT:
            _bool = True;
    return _bool;

def keyboard_check(key,type:str|None="pressed"):
    if key not in key_status:
        key_status[key] = {"pressed":False,"down":False,"up":False};
    if key_status[key]["down"]: key_status[key]["down"] = False;
    if key_status[key]["up"]: key_status[key]["up"] = False;
    for event in events:
        if event.type == pygame.KEYDOWN:
            if event.key == key:
                key_status[key]["pressed"] = True;
                key_status[key]["down"] = True;
        if event.type == pygame.KEYUP:
            if event.key == key:
                key_status[key]["pressed"] = False;
                key_status[key]["up"] = True;
    return key_status[key][type];

def init_render(background_color:str|None="black"):
    screen.fill(background_color);

def final_render():
    global dt
    pygame.display.flip();
    dt = clock.tick(60)/100;

# def draw_2d(type:str,position:pygame.Vector2,color:str,radio:int):
#     match type:
#         case "circle":
#             pygame.draw.circle(screen,color,position,radio);
#         case "polygon":
#             pygame.draw.polygon(screen,color,position,radio);

def draw_circle(position:pygame.Vector2,color:str,radius:int):
    pygame.draw.circle(screen,color,position,radius);

def draw_polygon(position:pygame.Vector2,color:str):
    pygame.draw.polygon();


class Coordinate:
    def __init__(self,x:int,y:int):
        self.x = x;
        self.y = y;
        self.vec = pygame.Vector2(self.x,self.y);
    def update(self,x:int|None=None,y:int|None=None):
        if x is not None: self.x = x;
        if y is not None: self.y = y;
        self.vec = pygame.Vector2(self.x,self.y);
    def goto(self,dir_or_guid:str,force:int):
        match dir_or_guid:
            case "vertical":
                self.y += force * dt;
            case "horizontal":
                self.x += force * dt;
            case "left":
                self.x -= force * dt;
            case "right":
                self.x += force * dt;
            case "up":
                self.y -= force * dt;
            case "down":
                self.y += force * dt;
        self.update();
    def __repr__(self):
        return f"({self.x},{self.y})";
    def __call__(self):
        self.update();
        return self.vec;
    def get_tuple(self):
        return (self.x,self.y);

class Entity:
    """
    Classe feita para entidades. Como players, npcs, mobs, inimigos, etc.
    
    Exemplo de Utilização:
    ```
    # Define o player como sendo uma entidade
    player = Entity((0,0)) # (0,0) é a posição do player. (x,y)
    ```
    """
    def __init__(self,init_position:Coordinate|None=None):
        if init_position is None:
            self.position = Coordinate(0,0);
        elif isinstance(init_position,tuple):
            self.position = Coordinate(init_position[0],init_position[1]);
        else:
            self.position = init_position;