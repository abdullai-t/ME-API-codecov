from _main_.utils.context import Context
from _main_.utils.massenergize_response import MassenergizeResponse
from _main_.utils.route_handler import RouteHandler
from api.services.technology import TechnologyService


class TechnologyHandler(RouteHandler):
    def __init__(self):
        super().__init__()
        self.service = TechnologyService()
        self.registerRoutes()

    def registerRoutes(self):
        self.add("/technologies.info", self.info)
        self.add("/technologies.create", self.create)
        self.add("/technologies.list", self.list)
        self.add("/technologies.update", self.update)
        self.add("/technologies.delete", self.delete)
        self.add("/technologies.coaches.add", self.add_coach)
        self.add("/technologies.coaches.remove", self.remove_coach)
        self.add("/technologies.listForAdmin", self.list_for_admin)
        self.add("/technologies.vendors.add", self.add_vendor)
        self.add("/technologies.vendors.remove", self.remove_vendor)
        self.add("/technologies.vendors.list", self.list_vendors)
        self.add("/technologies.overview.create", self.create_overview)
        self.add("/technologies.overview.update", self.update_overview)
        self.add("/technologies.overview.delete", self.delete_overview)
        self.add("/technologies.overview.list", self.list_overviews)



    def info(self, request):
        context: Context = request.context
        args: dict = context.args

        self.validator.expect("id", str, is_required=True)

        args, err = self.validator.verify(args, strict=True)
        if err:
            return err

        res, err = self.service.get_technology_info(context, args)
        if err:
            return err
        return MassenergizeResponse(data=res)
    

    def list(self, request):
        context: Context = request.context
        args: dict = context.args

        res, err = self.service.list_technologies(context, args)
        if err:
            return err
        return MassenergizeResponse(data=res)
    


    def create(self, request):
        context: Context = request.context
        args: dict = context.args

        self.validator.expect("name", str, is_required=True)
        self.validator.expect("description", str, is_required=True)
        self.validator.expect("image", str, is_required=True)

        args, err = self.validator.verify(args, strict=True)

        if err:
            return err 
        
        res, err = self.service.create_technology(context, args)
        if err:
            return err
        return MassenergizeResponse(data=res)
    

    def update(self, request):
        context: Context = request.context
        args: dict = context.args

        self.validator.expect("id", str, is_required=True)
        self.validator.expect("name", str, is_required=False)
        self.validator.expect("description", str, is_required=False)
        self.validator.expect("image", str, is_required=False)


        args, err = self.validator.verify(args, strict=True)

        if err:
            return err 
        
        res, err = self.service.update_technology(context, args)
        if err:
            return err
        return MassenergizeResponse(data=res)
    

    def delete(self, request):
        context: Context = request.context
        args: dict = context.args

        self.validator.expect("id", str, is_required=True)

        args, err = self.validator.verify(args, strict=True)

        if err:
            return err 
        
        res, err = self.service.delete_technology(context, args)
        if err:
            return err
        return MassenergizeResponse(data=res)
    


    def list_for_admin(self, request):
        context: Context = request.context
        args: dict = context.args

        res, err = self.service.list_technologies_for_admin(context, args)  
        if err:
            return err
        return MassenergizeResponse(data=res)
    

    def add_coach(self, request):
        context: Context = request.context
        args: dict = context.args

        self.validator.expect("technology_id", str, is_required=True)
        self.validator.expect("user_id", str, is_required=True)

        args, err = self.validator.verify(args, strict=True)

        if err:
            return err 
        
        res, err = self.service.add_technology_coach(context, args)
        if err:
            return err
        return MassenergizeResponse(data=res)
    

    def remove_coach(self, request):
        context: Context = request.context
        args: dict = context.args

        self.validator.expect("technology_id", str, is_required=True)
        self.validator.expect("user_id", str, is_required=True)

        args, err = self.validator.verify(args, strict=True)

        if err:
            return err 
        
        res, err = self.service.remove_technology_coach(context, args)
        if err:
            return err
        return MassenergizeResponse(data=res)
    

    def add_vendor(self, request):
        context: Context = request.context
        args: dict = context.args

        self.validator.expect("technology_id", str, is_required=True)
        self.validator.expect("vendor_id", str, is_required=True)

        args, err = self.validator.verify(args, strict=True)

        if err:
            return err 
        
        res, err = self.service.add_technology_vendor(context, args)
        if err:
            return err
        return MassenergizeResponse(data=res)
    

    def remove_vendor(self, request):
        context: Context = request.context
        args: dict = context.args

        self.validator.expect("technology_id", str, is_required=True)
        self.validator.expect("vendor_id", str, is_required=True)

        args, err = self.validator.verify(args, strict=True)

        if err:
            return err 
        
        res, err = self.service.remove_technology_vendor(context, args)
        if err:
            return err
        return MassenergizeResponse(data=res)
    

    def create_overview(self, request):
        context: Context = request.context
        args: dict = context.args

        self.validator.expect("technology_id", str, is_required=True)
        self.validator.expect("title", str, is_required=True)
        self.validator.expect("description", str, is_required=True)
        self.validator.expect("image", str, is_required=True)

        args, err = self.validator.verify(args, strict=True)

        if err:
            return err 
        
        res, err = self.service.create_technology_overview(context, args)
        if err:
            return err
        return MassenergizeResponse(data=res)
    

    def update_overview(self, request):
        context: Context = request.context
        args: dict = context.args

        self.validator.expect("id", str, is_required=True)
        self.validator.expect("title", str, is_required=False)
        self.validator.expect("description", str, is_required=False)
        self.validator.expect("image", str, is_required=False)

        args, err = self.validator.verify(args, strict=True)

        if err:
            return err 
        
        res, err = self.service.update_technology_overview(context, args)
        if err:
            return err
        return MassenergizeResponse(data=res)
    

    def delete_overview(self, request):
        context: Context = request.context
        args: dict = context.args

        self.validator.expect("id", str, is_required=True)

        args, err = self.validator.verify(args, strict=True)

        if err:
            return err 
        
        res, err = self.service.delete_technology_overview(context, args)
        if err:
            return err
        return MassenergizeResponse(data=res)
    


    def list_overviews(self, request):
        context: Context = request.context
        args: dict = context.args

        self.validator.expect("technology_id", str, is_required=True)

        args, err = self.validator.verify(args, strict=True)

        if err:
            return err 
        
        res, err = self.service.list_technology_overviews(context, args)
        if err:
            return err
        return MassenergizeResponse(data=res)
    

    def list_vendors(self, request):
        context: Context = request.context
        args: dict = context.args

        self.validator.expect("technology_id", str, is_required=True)

        args, err = self.validator.verify(args, strict=True)

        if err:
            return err 
        
        res, err = self.service.list_technology_vendors(context, args)
        if err:
            return err
        return MassenergizeResponse(data=res)
