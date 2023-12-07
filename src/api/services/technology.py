

from _main_.utils.common import serialize, serialize_all
from _main_.utils.context import Context
from _main_.utils.massenergize_errors import MassEnergizeAPIError
from typing import Tuple

from api.store.technology import TechnologyStore


class TechnologyService:
    """
    Service Layer for all the technologies
    """

    def __init__(self):
        self.store =  TechnologyStore()

    def get_technology_info(self, context: Context, args) -> Tuple[dict, MassEnergizeAPIError]:
        res, err = self.store.get_technology_info(context, args)
        if err:
             return None, err
        return serialize(res, full=True), None
    
    def list_technologies(self, context: Context, args) -> Tuple[list, MassEnergizeAPIError]:
        res, err = self.store.list_technologies(context, args)
        if err:
            return None, err
        return serialize_all(res, full=True), None

    def create_technology(self, context: Context, args) -> Tuple[dict, MassEnergizeAPIError]:
        res, err = self.store.create_technology(context, args)
        if err:
            return None, err
        
        return serialize(res, full=True), None
    

    def update_technology(self, context: Context, args) -> Tuple[dict, MassEnergizeAPIError]:
        res, err = self.store.update_technology(context, args)
        if err:
            return None, err
        return serialize(res, full=True), None
    

    def delete_technology(self, context: Context, args) -> Tuple[dict, MassEnergizeAPIError]:
        technology, err = self.store.delete_technology(context, args)
        if err:
            return None, err
        return serialize(technology), None
    

    def list_technologies_for_admin(self, context: Context, args) -> Tuple[list, MassEnergizeAPIError]:
        technologies, err = self.store.list_technologies_for_admin(context, args)
        if err:
            return None, err
        return serialize_all(technologies), None
    
    def add_technology_coach(self,  context: Context, args) -> Tuple[list, MassEnergizeAPIError]:
        res, err = self.store.add_technology_coach(context, args)
        if err:
            return None, err
        return serialize(res), None
    
    def remove_technology_coach(self,  context: Context, args) -> Tuple[list, MassEnergizeAPIError]:
        res, err = self.store.remove_technology_coach(context, args)
        if err:
            return None, err
        return serialize(res), None
    
    def add_technology_vendor(self,  context: Context, args) -> Tuple[list, MassEnergizeAPIError]:
        res, err = self.store.add_technology_vendor(context, args)
        if err:
            return None, err
        return serialize(res), None
    
    def remove_technology_vendor(self,  context: Context, args) -> Tuple[list, MassEnergizeAPIError]:
        res, err = self.store.remove_technology_vendor(context, args)
        if err:
            return None, err
        return serialize(res), None
    
    def create_technology_overview(self,  context: Context, args) -> Tuple[list, MassEnergizeAPIError]:
        res, err = self.store.add_technology_overview(context, args)
        if err:
            return None, err
        return serialize(res), None
    
    def update_technology_overview(self,  context: Context, args) -> Tuple[list, MassEnergizeAPIError]:
        res, err = self.store.update_technology_overview(context, args)
        if err:
            return None, err
        return serialize(res), None
    
    def delete_technology_overview(self,  context: Context, args) -> Tuple[list, MassEnergizeAPIError]:
        res, err = self.store.delete_technology_overview(context, args)
        if err:
            return None, err
        return serialize(res), None
    
    def list_technology_overviews(self,  context: Context, args) -> Tuple[list, MassEnergizeAPIError]:
        res, err = self.store.list_technology_overviews(context, args)
        if err:
            return None, err
        return serialize_all(res), None
    
    def list_technology_vendors(self,  context: Context, args) -> Tuple[list, MassEnergizeAPIError]:
        res, err = self.store.list_technology_vendors(context, args)
        if err:
            return None, err
        return serialize_all(res), None
    

    def list_technologies_for_admin(self, context: Context, args) -> Tuple[list, MassEnergizeAPIError]:
        technologies, err = self.store.list_technologies_for_admin(context, args)
        if err:
            return None, err
        return serialize_all(technologies), None