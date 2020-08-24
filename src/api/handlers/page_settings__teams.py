"""Handler file for all routes pertaining to teams_page_settings"""

from _main_.utils.route_handler import RouteHandler
from _main_.utils.common import get_request_contents, rename_field
from api.services.page_settings__teams import TeamsPageSettingsService
from _main_.utils.massenergize_response import MassenergizeResponse
from types import FunctionType as function
from _main_.utils.context import Context
from _main_.utils.validator import Validator


#TODO: install middleware to catch authz violations
#TODO: add logger

class TeamsPageSettingsHandler(RouteHandler):

  def __init__(self):
    super().__init__()
    self.service = TeamsPageSettingsService()
    self.registerRoutes()

  def registerRoutes(self) -> None:
    self.add("/teams_page_settings.info", self.info()) 
    self.add("/teams_page_settings.create", self.create())
    self.add("/teams_page_settings.add", self.create())
    self.add("/teams_page_settings.list", self.list())
    self.add("/teams_page_settings.update", self.update())
    self.add("/teams_page_settings.delete", self.delete())
    self.add("/teams_page_settings.remove", self.delete())

    #admin routes
    self.add("/teams_page_settings.listForCommunityAdmin", self.community_admin_list())
    self.add("/teams_page_settings.listForSuperAdmin", self.super_admin_list())


  def info(self) -> function:
    def teams_page_setting_info_view(request) -> None: 
      context: Context = request.context
      args: dict = context.args
      args = rename_field(args, 'community_id', 'community__id')
      args = rename_field(args, 'subdomain', 'community__subdomain')
      args = rename_field(args, 'teams_page_id', 'id')
      teams_page_setting_info, err = self.service.get_teams_page_setting_info(args)
      if err:
        return MassenergizeResponse(error=str(err), status=err.status)
      return MassenergizeResponse(data=teams_page_setting_info)
    return teams_page_setting_info_view


  def create(self) -> function:
    def create_teams_page_setting_view(request) -> None: 
      context: Context = request.context
      args: dict = context.args
      teams_page_setting_info, err = self.service.create_teams_page_setting(args)
      if err:
        return MassenergizeResponse(error=str(err), status=err.status)
      return MassenergizeResponse(data=teams_page_setting_info)
    return create_teams_page_setting_view


  def list(self) -> function:
    def list_teams_page_setting_view(request) -> None: 
      context: Context = request.context
      args: dict = context.args
      community_id = args.pop('community_id', None)
      user_id = args.pop('user_id', None)
      teams_page_setting_info, err = self.service.list_teams_page_settings(community_id, user_id)
      if err:
        return MassenergizeResponse(error=str(err), status=err.status)
      return MassenergizeResponse(data=teams_page_setting_info)
    return list_teams_page_setting_view


  def update(self) -> function:
    def update_teams_page_setting_view(request) -> None: 
      context: Context = request.context
      args: dict = context.args
      teams_page_setting_info, err = self.service.update_teams_page_setting(args)
      if err:
        return MassenergizeResponse(error=str(err), status=err.status)
      return MassenergizeResponse(data=teams_page_setting_info)
    return update_teams_page_setting_view


  def delete(self) -> function:
    def delete_teams_page_setting_view(request) -> None: 
      context: Context = request.context
      args: dict = context.args
      teams_page_setting_id = args.get("id", None)
      teams_page_setting_info, err = self.service.delete_teams_page_setting(args.get("id", None))
      if err:
        return MassenergizeResponse(error=str(err), status=err.status)
      return MassenergizeResponse(data=teams_page_setting_info)
    return delete_teams_page_setting_view


  def community_admin_list(self) -> function:
    def community_admin_list_view(request) -> None: 
      context: Context = request.context
      args: dict = context.args
      community_id = args.pop("community_id", None)
      teams_page_settings, err = self.service.list_teams_page_settings_for_community_admin(community_id)
      if err:
        return MassenergizeResponse(error=str(err), status=err.status)
      return MassenergizeResponse(data=teams_page_settings)
    return community_admin_list_view


  def super_admin_list(self) -> function:
    def super_admin_list_view(request) -> None: 
      context: Context = request.context
      args: dict = context.args
      teams_page_settings, err = self.service.list_teams_page_settings_for_super_admin()
      if err:
        return MassenergizeResponse(error=str(err), status=err.status)
      return MassenergizeResponse(data=teams_page_settings)
    return super_admin_list_view