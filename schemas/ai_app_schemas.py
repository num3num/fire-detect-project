from pydantic import BaseModel,Field
from typing import Optional,List,Union,List
from schemas.base import BaseResp, ResAntTable

class AIApp(BaseModel):
    appid: str=Field(...,title="appid",description="appid")
    app_key: Optional[str]=Field(title="app_key",description="app_key",default=None)
    app_secret: Optional[str]=Field(title="app_secret",description="app_secret", default=None)
    app_name: Optional[str]=Field(title="app_name",description="app_name", default=None)
    userid: Optional[int]=Field(title="userid",description="userid", default=None)
    mark: Optional[str]=Field(title="备注",description="备注", default=None)
    status: Optional[int]=Field(title="1=正常 0=禁用",description="1=正常 0=禁用", default=1)
    create_time: Optional[str]=Field(title="create_time",description="create_time", default=None)

class AddAIApp(BaseModel):
    app_name: str=Field(...,title="app_name",description="app_name",max_length=32)
    mark: Optional[str]=Field(title="备注",description="备注", default=None,max_length=256)

class AIApps(BaseResp):
    data:List[AIApp]

class AIAppDetail(BaseResp):
    data:List[AIApp]
