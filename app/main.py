from fastapi import Depends, FastAPI, Request, Depends
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from .util.variables import cors_config, templates
from .util.database import lifetime
from .util.auth import CookieInitializationMiddleware, get_current_user
from .login import router as LoginRoute
from .register import router as RegisterRoute


app = FastAPI(lifespan=lifetime)

app.mount("/img", StaticFiles(directory=f"./app/static/img"), name="img")
app.add_middleware(CORSMiddleware, **cors_config)
app.add_middleware(CookieInitializationMiddleware)
app.include_router(LoginRoute)
app.include_router(RegisterRoute)


@app.get("/")
async def getDashBoard(request: Request, session: str = Depends(get_current_user)):
    cards = {
        'row1': {
            'Clientes Registrados': 17,
            'Serviços Ativos': 8,
            'Saldo Atual': 'R$ 1507,89'
        },
        'row2': {
            'Entrada': {
                'Entrada Consolidada': 'R$ 107,89',
                'Entrada Prevista': 'R$ 1507,89' ,
            },
            'Saída': {
                'Saída Consolidada': 'R$ 107,89',
                'Saída Prevista': 'R$ 1507,89' ,
            },
            'Saldo do Mês': {
                'Saldo Consolidado': 'R$ 107,89',
                'Saldo Previsto': 'R$ 900,89' ,
            }
        }
    }
    sidebar = {
        'user': {
            'title': 'Usuário',
            'children': {
                'perfil': 'Perfil',
                'template': 'Templates',
                'logout': 'Logout'
            }
            
        },
        'clients' : {
            'title': 'Clientes',
            'children': {
                'pf':'Pessoa Física',
                'pj': 'Pessoa Jurídica'
                }
            },
        'services': {
            'title': 'Serviços',
            'children': {
                'investigation': 'Investigação',
                'process': 'Processos',
                'consult': 'Consultoria'
            }
        },
        'schedule': {
            'title': 'Agenda',
            'children': {
                'from_user': 'From User',
                'from_services': 'From Services',
                'from_action': 'From Actions' 
            }
        }
    }
    return templates.TemplateResponse(
        request=request,
        name='dashboard.html',
        context={
            'sidebar': sidebar,
            'card': cards
        }
    )
