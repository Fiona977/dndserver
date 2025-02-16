# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: Lobby.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import _Character_pb2 as __Character__pb2
import _Item_pb2 as __Item__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0bLobby.proto\x12\tDC.Packet\x1a\x10_Character.proto\x1a\x0b_Item.proto\"!\n\x1fSC2S_CHARACTER_SELECT_ENTER_REQ\"1\n\x1fSS2C_CHARACTER_SELECT_ENTER_RES\x12\x0e\n\x06result\x18\x01 \x01(\r\"\x1f\n\x1dSC2S_LOBBY_CHARACTER_INFO_REQ\"f\n\x1dSS2C_LOBBY_CHARACTER_INFO_RES\x12\x0e\n\x06result\x18\x01 \x01(\r\x12\x35\n\x11\x63haracterDataBase\x18\x02 \x01(\x0b\x32\x1a.DC.Packet.SCHARACTER_INFO\"\x19\n\x17SC2S_OPEN_LOBBY_MAP_REQ\"\x19\n\x17SS2C_OPEN_LOBBY_MAP_RES\".\n\x1cSC2S_LOBBY_REGION_SELECT_REQ\x12\x0e\n\x06region\x18\x01 \x01(\r\">\n\x1cSS2C_LOBBY_REGION_SELECT_RES\x12\x0e\n\x06result\x18\x01 \x01(\r\x12\x0e\n\x06region\x18\x02 \x01(\r\" \n\x1eSC2S_LOBBY_ENTER_FROM_GAME_REQ\"0\n\x1eSS2C_LOBBY_ENTER_FROM_GAME_RES\x12\x0e\n\x06result\x18\x01 \x01(\r\"H\n%SC2S_LOBBY_GAME_DIFFICULTY_SELECT_REQ\x12\x1f\n\x17gameDifficultyTypeIndex\x18\x01 \x01(\r\"X\n%SS2C_LOBBY_GAME_DIFFICULTY_SELECT_RES\x12\x0e\n\x06result\x18\x01 \x01(\r\x12\x1f\n\x17gameDifficultyTypeIndex\x18\x02 \x01(\r\"E\n\x16SACCOUNT_CURRENCY_INFO\x12\x14\n\x0c\x63urrencyType\x18\x01 \x01(\r\x12\x15\n\rcurrencyValue\x18\x02 \x01(\r\"`\n$SS2C_LOBBY_ACCOUNT_CURRENCY_LIST_NOT\x12\x38\n\rcurrencyInfos\x18\x01 \x03(\x0b\x32!.DC.Packet.SACCOUNT_CURRENCY_INFO\"a\n$SS2C_LOBBY_CHARACTER_LOBBY_EMOTE_NOT\x12\x39\n\x0elobbyEmoteList\x18\x01 \x03(\x0b\x32!.DC.Packet.SCUSTOMIZE_LOBBY_EMOTE\"E\n\x13SREPORT_PUNISH_INFO\x12.\n\x08nickname\x18\x01 \x01(\x0b\x32\x1c.DC.Packet.SACCOUNT_NICKNAME\"R\n!SS2C_LOBBY_REPORT_PUNISH_LIST_NOT\x12-\n\x05infos\x18\x01 \x03(\x0b\x32\x1e.DC.Packet.SREPORT_PUNISH_INFO\"0\n SC2S_LOBBY_ENTER_COUPON_CODE_REQ\x12\x0c\n\x04\x63ode\x18\x01 \x01(\t\"2\n SS2C_LOBBY_ENTER_COUPON_CODE_RES\x12\x0e\n\x06result\x18\x01 \x01(\rB\x1c\n\x11\x63om.packets.lobbyB\x05lobbyP\x00\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'Lobby_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\021com.packets.lobbyB\005lobbyP\000'
  _globals['_SC2S_CHARACTER_SELECT_ENTER_REQ']._serialized_start=57
  _globals['_SC2S_CHARACTER_SELECT_ENTER_REQ']._serialized_end=90
  _globals['_SS2C_CHARACTER_SELECT_ENTER_RES']._serialized_start=92
  _globals['_SS2C_CHARACTER_SELECT_ENTER_RES']._serialized_end=141
  _globals['_SC2S_LOBBY_CHARACTER_INFO_REQ']._serialized_start=143
  _globals['_SC2S_LOBBY_CHARACTER_INFO_REQ']._serialized_end=174
  _globals['_SS2C_LOBBY_CHARACTER_INFO_RES']._serialized_start=176
  _globals['_SS2C_LOBBY_CHARACTER_INFO_RES']._serialized_end=278
  _globals['_SC2S_OPEN_LOBBY_MAP_REQ']._serialized_start=280
  _globals['_SC2S_OPEN_LOBBY_MAP_REQ']._serialized_end=305
  _globals['_SS2C_OPEN_LOBBY_MAP_RES']._serialized_start=307
  _globals['_SS2C_OPEN_LOBBY_MAP_RES']._serialized_end=332
  _globals['_SC2S_LOBBY_REGION_SELECT_REQ']._serialized_start=334
  _globals['_SC2S_LOBBY_REGION_SELECT_REQ']._serialized_end=380
  _globals['_SS2C_LOBBY_REGION_SELECT_RES']._serialized_start=382
  _globals['_SS2C_LOBBY_REGION_SELECT_RES']._serialized_end=444
  _globals['_SC2S_LOBBY_ENTER_FROM_GAME_REQ']._serialized_start=446
  _globals['_SC2S_LOBBY_ENTER_FROM_GAME_REQ']._serialized_end=478
  _globals['_SS2C_LOBBY_ENTER_FROM_GAME_RES']._serialized_start=480
  _globals['_SS2C_LOBBY_ENTER_FROM_GAME_RES']._serialized_end=528
  _globals['_SC2S_LOBBY_GAME_DIFFICULTY_SELECT_REQ']._serialized_start=530
  _globals['_SC2S_LOBBY_GAME_DIFFICULTY_SELECT_REQ']._serialized_end=602
  _globals['_SS2C_LOBBY_GAME_DIFFICULTY_SELECT_RES']._serialized_start=604
  _globals['_SS2C_LOBBY_GAME_DIFFICULTY_SELECT_RES']._serialized_end=692
  _globals['_SACCOUNT_CURRENCY_INFO']._serialized_start=694
  _globals['_SACCOUNT_CURRENCY_INFO']._serialized_end=763
  _globals['_SS2C_LOBBY_ACCOUNT_CURRENCY_LIST_NOT']._serialized_start=765
  _globals['_SS2C_LOBBY_ACCOUNT_CURRENCY_LIST_NOT']._serialized_end=861
  _globals['_SS2C_LOBBY_CHARACTER_LOBBY_EMOTE_NOT']._serialized_start=863
  _globals['_SS2C_LOBBY_CHARACTER_LOBBY_EMOTE_NOT']._serialized_end=960
  _globals['_SREPORT_PUNISH_INFO']._serialized_start=962
  _globals['_SREPORT_PUNISH_INFO']._serialized_end=1031
  _globals['_SS2C_LOBBY_REPORT_PUNISH_LIST_NOT']._serialized_start=1033
  _globals['_SS2C_LOBBY_REPORT_PUNISH_LIST_NOT']._serialized_end=1115
  _globals['_SC2S_LOBBY_ENTER_COUPON_CODE_REQ']._serialized_start=1117
  _globals['_SC2S_LOBBY_ENTER_COUPON_CODE_REQ']._serialized_end=1165
  _globals['_SS2C_LOBBY_ENTER_COUPON_CODE_RES']._serialized_start=1167
  _globals['_SS2C_LOBBY_ENTER_COUPON_CODE_RES']._serialized_end=1217
# @@protoc_insertion_point(module_scope)
