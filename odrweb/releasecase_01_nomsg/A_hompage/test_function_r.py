# coding: utf-8
import sys
import unittest
from datetime import datetime
from odrweb.core.initdata import init
from odrweb.page.browserinstance import BrowserWhole
from odrweb.page.homepage import HomePage
from odrweb.page.nologinhomepage import NoLoginHomePage


class HomepageNoLogin(unittest.TestCase):
    """未登录首页基本操作"""

    def setUp(self):
        self.homepage = HomePage()
        print "\n--------------------"

    def tearDown(self):
        self.homepage.driver.quit()

    def test_01(self):
        """服务内容-法律咨询-在线咨询-聊天对话"""
        nologinpage = NoLoginHomePage(self.homepage)
        nologinpage.get_url()
        nologinpage.head_service_online()
        nologinpage.change_windows()
        res = nologinpage.verification_head_service_online_chat()
        self.assertEqual(True, res)

    def test_02(self):
        """服务内容-法律咨询-在线咨询-法律咨询"""
        nologinpage = NoLoginHomePage(self.homepage)
        nologinpage.get_url()
        nologinpage.head_service_online()
        nologinpage.change_windows()
        nologinpage.head_service_online_law()
        res = nologinpage.verification_head_service_online_law()
        self.assertEqual(True, res)

    def test_03(self):
        """服务内容-法律咨询-在线咨询-解纷方式"""
        nologinpage = NoLoginHomePage(self.homepage)
        nologinpage.get_url()
        nologinpage.head_service_online()
        nologinpage.change_windows()
        nologinpage.head_service_online_way()
        res = nologinpage.verification_head_service_online_way()
        self.assertEqual(True, res)

    def test_04(self):
        """服务内容-法律咨询-在线咨询-相关案例"""
        nologinpage = NoLoginHomePage(self.homepage)
        nologinpage.get_url()
        nologinpage.head_service_online()
        nologinpage.change_windows()
        nologinpage.head_service_online_case()
        res = nologinpage.verification_head_service_online_case()
        self.assertEqual(True, res)

    def test_05(self):
        """服务内容-法律咨询-在线咨询-辅助工具"""
        nologinpage = NoLoginHomePage(self.homepage)
        nologinpage.get_url()
        nologinpage.head_service_online()
        nologinpage.change_windows()
        nologinpage.head_service_online_assist()
        res = nologinpage.verification_head_service_online_assist()
        self.assertEqual(True, res)

    def test_06(self):
        """服务内容-法律咨询-在线咨询-登陆咨询"""
        nologinpage = NoLoginHomePage(self.homepage)
        nologinpage.get_url()
        nologinpage.head_service_manwork_login()
        res = nologinpage.verification_skip_login_page()
        self.assertEqual(True, res)

    def test_07(self):
        """服务内容-法律咨询-在线咨询-直接咨询-进入咨询
        """
        now_hour = int(datetime.now().strftime("%H"))
        if (now_hour >= 9) and (now_hour < 17):
            consult = {"consult_desc": u"假冒伪劣", "consult_ask": u"假一赔十"}
            nologinpage = NoLoginHomePage(self.homepage)
            nologinpage.get_url()
            nologinpage.head_service_manwork_consult(**consult)
            res = nologinpage.verification_head_service_manwork_consult(
                **consult)
            self.assertEqual(True, res)

    def test_08(self):
        """服务内容-在线评估"""
        nologinpage = NoLoginHomePage(self.homepage)
        nologinpage.get_url()
        nologinpage.head_service_assessment()
        res = nologinpage.verification_skip_login_page()  # 校验方法为跳转登录页面
        self.assertEqual(True, res)

    def test_09(self):
        """服务内容-在线调解-调解类别-申请调解"""
        nologinpage = NoLoginHomePage(self.homepage)
        nologinpage.get_url()
        nologinpage.head_dispute_type_dispute()
        res = nologinpage.verification_skip_login_page()  # 校验方法为跳转登录页面
        self.assertEqual(True, res)

    def test_10(self):
        """服务内容-在线调解-调解类别-法律咨询"""
        nologinpage = NoLoginHomePage(self.homepage)
        nologinpage.get_url()
        nologinpage.head_dispute_type_consult()
        nologinpage.change_windows()
        res = nologinpage.verification_head_service_online_chat(
        )  # 验证方法为验证进入智能机器人
        self.assertEqual(True, res)

    def test_11(self):
        """服务内容-在线调解-纠纷调解中心-婚姻家事"""
        nologinpage = NoLoginHomePage(self.homepage)
        nologinpage.get_url()
        nologinpage.head_dispute_center_marriage()
        res = nologinpage.verification_fjb_service_url()
        self.assertEqual(True, res)

    def test_12(self):
        """服务内容-在线调解-纠纷调解中心-道路纠纷"""
        nologinpage = NoLoginHomePage(self.homepage)
        nologinpage.get_url()
        nologinpage.head_dispute_center_traffic()
        res = nologinpage.verification_jtsp_traffic_url()
        self.assertEqual(True, res)

    def test_13(self):
        """服务内容-在线调解-纠纷调解中心-律师调解中心"""
        nologinpage = NoLoginHomePage(self.homepage)
        nologinpage.get_url()
        nologinpage.head_dispute_center_lawer()
        res = nologinpage.verifivation_head_dispute_center_lawer()
        self.assertEqual(True, res)

    def test_14(self):
        """服务内容-仲裁服务"""
        nologinpage = NoLoginHomePage(self.homepage)
        nologinpage.get_url()
        nologinpage.head_service_arbitration()
        nologinpage.change_windows()
        res = nologinpage.verification_arbitration()
        self.assertEqual(True, res)

    def test_15(self):
        """服务内容-诉讼服务"""
        nologinpage = NoLoginHomePage(self.homepage)
        nologinpage.get_url()
        nologinpage.head_service_lawshit()
        res = nologinpage.verification_lawshit()
        self.assertEqual(True, res)

    def test_16(self):
        """服务资源-机构资源-机构详情"""
        nologinpage = NoLoginHomePage(self.homepage)
        nologinpage.get_url()
        ogr_name_11, ogr_name_12 = nologinpage.head_resource_organization_info(
        )
        res = nologinpage.verification_head_resource_organization_info(
            ogr_name_11, ogr_name_12)
        self.assertEqual(True, res)

    def test_17(self):
        """服务资源-机构资源-机构搜索"""
        nologinpage = NoLoginHomePage(self.homepage)
        nologinpage.get_url()
        ogr_name_21, ogr_name_22 = nologinpage.head_resource_organization_search(
        )
        res = nologinpage.verification_head_resource_organization_search(
            ogr_name_21, ogr_name_22)
        self.assertEqual(True, res)

    def test_18(self):
        """服务资源-服务人员-服务人员详情"""
        nologinpage = NoLoginHomePage(self.homepage)
        nologinpage.get_url()
        per_name_11, per_name_12 = nologinpage.head_resource_serpersonal_info()
        res = nologinpage.verification_head_resource_serpersonal_info(
            per_name_11, per_name_12)
        self.assertEqual(True, res)

    def test_19(self):
        """服务资源-服务人员-服务人员搜索"""
        nologinpage = NoLoginHomePage(self.homepage)
        nologinpage.get_url()
        per_name_21, per_name_22 = nologinpage.head_resource_serpersonal_search(
        )
        res = nologinpage.verification_head_resource_serpersonal_search(
            per_name_21, per_name_22)
        self.assertEqual(True, res)

    def test_20(self):
        """服务资源-服务人员-更多擅长领域"""
        nologinpage = NoLoginHomePage(self.homepage)
        nologinpage.get_url()
        nologinpage.head_resource_serpersonal_more()
        res = nologinpage.verification_head_resource_serpersonal_more()
        self.assertEqual(True, res)

    def test_21(self):
        """新闻动态"""
        nologinpage = NoLoginHomePage(self.homepage)
        nologinpage.get_url()
        title_1, title_2 = nologinpage.head_news()
        res = nologinpage.verification_head_news(title_1, title_2)
        self.assertEqual(True, res)

    def test_22(self):
        """帮助中心-常见问题-新手指南-用户注册"""
        nologinpage = NoLoginHomePage(self.homepage)
        nologinpage.get_url()
        nologinpage.head_help_common_enrol()
        res = nologinpage.verification_head_help_common()
        self.assertEqual(True, res)

    def test_23(self):
        """帮助中心-常见问题-新手指南-用户登陆"""
        nologinpage = NoLoginHomePage(self.homepage)
        nologinpage.get_url()
        nologinpage.head_help_common_login()
        res = nologinpage.verification_head_help_common()
        self.assertEqual(True, res)

    def test_24(self):
        """帮助中心-常见问题-新手指南-忘记密码"""
        nologinpage = NoLoginHomePage(self.homepage)
        nologinpage.get_url()
        nologinpage.head_help_common_password()
        res = nologinpage.verification_head_help_common()
        self.assertEqual(True, res)

    def test_25(self):
        """帮助中心-常见问题-新手指南-用户注册协议"""
        nologinpage = NoLoginHomePage(self.homepage)
        nologinpage.get_url()
        nologinpage.head_help_common_agreement()
        res = nologinpage.verification_head_help_common()
        self.assertEqual(True, res)

    def test_26(self):
        """帮助中心-常见问题-平台服务-纠纷调解服务"""
        nologinpage = NoLoginHomePage(self.homepage)
        nologinpage.get_url()
        nologinpage.head_help_common_mediate()
        res = nologinpage.verification_head_help_common_mediate()
        self.assertEqual(True, res)

    def test_27(self):
        """帮助中心-常见问题-平台服务-法律咨询服务"""
        nologinpage = NoLoginHomePage(self.homepage)
        nologinpage.get_url()
        nologinpage.head_help_common_consult()
        res = nologinpage.verification_head_help_common_consult()
        self.assertEqual(True, res)

    def test_28(self):
        """帮助中心-常见问题-平台服务-在线评估服务"""
        nologinpage = NoLoginHomePage(self.homepage)
        nologinpage.get_url()
        nologinpage.head_help_common_assess()
        res = nologinpage.verification_head_help_common_assess()
        self.assertEqual(True, res)

    def test_29(self):
        """帮助中心-常见问题-平台服务-服务资源"""
        nologinpage = NoLoginHomePage(self.homepage)
        nologinpage.get_url()
        nologinpage.head_help_common_services()
        res = nologinpage.verification_head_help_common_services()
        self.assertEqual(True, res)

    def test_30(self):
        """帮助中心-常见问题-使用流程-申请调解"""
        nologinpage = NoLoginHomePage(self.homepage)
        nologinpage.get_url()
        nologinpage.head_help_common_apply()
        res = nologinpage.verification_head_help_common_apply()
        self.assertEqual(True, res)

    def test_31(self):
        """帮助中心-常见问题-使用流程-在线评估"""
        nologinpage = NoLoginHomePage(self.homepage)
        nologinpage.get_url()
        nologinpage.head_help_common_online()
        res = nologinpage.verification_head_help_common_online()
        self.assertEqual(True, res)

    def test_32(self):
        """帮助中心-常见问题-使用流程-在线咨询"""
        nologinpage = NoLoginHomePage(self.homepage)
        nologinpage.get_url()
        nologinpage.head_help_common_law()
        res = nologinpage.verification_head_help_common_law()
        self.assertEqual(True, res)

    def test_33(self):
        """帮助中心-常见问题-使用流程-查看结果"""
        nologinpage = NoLoginHomePage(self.homepage)
        nologinpage.get_url()
        nologinpage.head_help_common_result()
        res = nologinpage.verification_head_help_common_result()
        self.assertEqual(True, res)

    def test_34(self):
        """帮助中心-常见问题-帐号设置-实名认证"""
        nologinpage = NoLoginHomePage(self.homepage)
        nologinpage.get_url()
        nologinpage.head_help_common_autonym()
        res = nologinpage.verification_head_help_common_autonym()
        self.assertEqual(True, res)

    def test_35(self):
        """帮助中心-常见问题-帐号设置-修改密码"""
        nologinpage = NoLoginHomePage(self.homepage)
        nologinpage.get_url()
        nologinpage.head_help_common_modification()
        res = nologinpage.verification_head_help_common_modification()
        self.assertEqual(True, res)

    def test_36(self):
        """帮助中心-常见问题-帐号设置-个人信息"""
        nologinpage = NoLoginHomePage(self.homepage)
        nologinpage.get_url()
        nologinpage.head_help_common_personal()
        res = nologinpage.verification_head_help_common_personal()
        self.assertEqual(True, res)

    def test_37(self):
        """帮助中心-常见问题-帐号设置-手写签名"""
        nologinpage = NoLoginHomePage(self.homepage)
        nologinpage.get_url()
        nologinpage.head_help_common_signature()
        res = nologinpage.verification_head_help_common_signature()
        self.assertEqual(True, res)

    def test_38(self):
        """帮助中心-自助服务-注册"""
        nologinpage = NoLoginHomePage(self.homepage)
        nologinpage.get_url()
        nologinpage.head_help_self_enrol()
        res = nologinpage.verification_head_help_self_enrol()
        self.assertEqual(True, res)

    def test_39(self):
        """帮助中心-自助服务-忘记密码"""
        nologinpage = NoLoginHomePage(self.homepage)
        nologinpage.get_url()
        nologinpage.head_help_self_forget()
        res = nologinpage.verification_head_help_self_forget()
        self.assertEqual(True, res)

    def test_40(self):
        """帮助中心-自助服务-实名认证"""
        nologinpage = NoLoginHomePage(self.homepage)
        nologinpage.get_url()
        nologinpage.head_help_self_redirect()
        res = nologinpage.verification_skip_login_page()  # 校验方法为跳转登录页面
        self.assertEqual(True, res)

    def test_41(self):
        """帮助中心-自助服务-法律咨询"""
        nologinpage = NoLoginHomePage(self.homepage)
        nologinpage.get_url()
        nologinpage.head_help_self_consult()
        res = nologinpage.verification_head_help_self_consult()
        self.assertEqual(True, res)

    def test_42(self):
        """帮助中心-自助服务-申请调解"""
        nologinpage = NoLoginHomePage(self.homepage)
        nologinpage.get_url()
        nologinpage.head_help_self_apply()
        res = nologinpage.verification_skip_login_page()  # 校验方法为跳转登录页面
        self.assertEqual(True, res)

    def test_43(self):
        """帮助中心-自助服务-在线评估"""
        nologinpage = NoLoginHomePage(self.homepage)
        nologinpage.get_url()
        nologinpage.head_help_self_assess()
        res = nologinpage.verification_skip_login_page()  # 校验方法为跳转登录页面
        self.assertEqual(True, res)

    def test_44(self):
        """帮助中心-自助服务-查看调解结果"""
        nologinpage = NoLoginHomePage(self.homepage)
        nologinpage.get_url()
        nologinpage.head_help_self_result()
        res = nologinpage.verification_skip_login_page()  # 校验方法为跳转登录页面
        self.assertEqual(True, res)

    def test_45(self):
        """帮助中心-在线咨询-智能机器人"""
        nologinpage = NoLoginHomePage(self.homepage)
        nologinpage.get_url()
        nologinpage.head_help_consult_robot()
        nologinpage.change_windows()
        res = nologinpage.verification_head_service_online_chat(
        )  # 验证方法为验证进入智能机器人
        self.assertEqual(True, res)

    def test_46(self):
        """帮助中心-常见问题"""
        nologinpage = NoLoginHomePage(self.homepage)
        nologinpage.get_url()
        nologinpage.head_help_comproblem()
        res = nologinpage.verification_head_help_common()  # 验证方法为帮助中心常见问题验证
        self.assertEqual(True, res)

    def test_47(self):
        """帮助中心-在线咨询"""
        nologinpage = NoLoginHomePage(self.homepage)
        nologinpage.get_url()
        nologinpage.head_help_online()
        nologinpage.change_windows()
        res = nologinpage.verification_head_service_online_chat(
        )  # 验证方法为验证进入智能机器人
        self.assertEqual(True, res)

    def test_48(self):
        """首页-法律咨询"""
        nologinpage = NoLoginHomePage(self.homepage)
        nologinpage.get_url()
        nologinpage.mid_law()
        res = nologinpage.verification_head_help_self_consult(
        )  # 验证方法为进入法律咨询校验方法
        self.assertEqual(True, res)

    def test_49(self):
        """首页-在线评估"""
        nologinpage = NoLoginHomePage(self.homepage)
        nologinpage.get_url()
        nologinpage.mid_assess()
        res = nologinpage.verification_skip_login_page()  # 验证方法为跳转登陆页面
        self.assertEqual(True, res)

    def test_50(self):
        """首页-在线调解"""
        nologinpage = NoLoginHomePage(self.homepage)
        nologinpage.get_url()
        nologinpage.mid_mediate()
        res = nologinpage.verification_mid_mediate()  # 验证方法为跳转登陆页面
        self.assertEqual(True, res)

    def test_51(self):
        """首页-仲裁服务"""
        nologinpage = NoLoginHomePage(self.homepage)
        nologinpage.get_url()
        nologinpage.mid_arbitration()
        nologinpage.change_windows()
        res = nologinpage.verification_arbitration()  # 验证方法为跳转仲裁服务网站URL
        self.assertEqual(True, res)

    def test_52(self):
        """首页-诉讼服务"""
        nologinpage = NoLoginHomePage(self.homepage)
        nologinpage.get_url()
        nologinpage.mid_lawshit()
        nologinpage.change_windows()
        res = nologinpage.verification_lawshit()  # 验证方法为跳转诉讼服务网站RRL
        self.assertEqual(True, res)

    def test_53(self):
        """首页-用户中心-如何申请调解"""
        nologinpage = NoLoginHomePage(self.homepage)
        nologinpage.get_url()
        nologinpage.tail_user_mediate()
        res = nologinpage.verification_head_help_common_apply(
        )  # 验证方法为进入常见问题申请调解
        self.assertEqual(True, res)

    def test_54(self):
        """首页-用户中心-如何快速咨询"""
        nologinpage = NoLoginHomePage(self.homepage)
        nologinpage.get_url()
        nologinpage.tail_user_consult()
        res = nologinpage.verification_head_help_common_law()  # 验证方法为进入常见问题法律咨询
        self.assertEqual(True, res)

    def test_55(self):
        """首页-用户中心-如何申请评估"""
        nologinpage = NoLoginHomePage(self.homepage)
        nologinpage.get_url()
        nologinpage.tail_user_assess()
        res = nologinpage.verification_head_help_common_online(
        )  # 验证方法为常见问题在线评估
        self.assertEqual(True, res)

    def test_56(self):
        """首页-用户中心-如何查看结果"""
        nologinpage = NoLoginHomePage(self.homepage)
        nologinpage.get_url()
        nologinpage.tail_user_result()
        res = nologinpage.verification_head_help_common_result(
        )  # 验证方法为常见问题查看结果
        self.assertEqual(True, res)

    def test_57(self):
        """首页-用户中心-调解中心"""
        nologinpage = NoLoginHomePage(self.homepage)
        nologinpage.get_url()
        nologinpage.tail_user_center()
        nologinpage.change_windows()
        res = nologinpage.verification_tail_user_center()  # 验证方法为跳转诉讼服务网站RRL
        self.assertEqual(True, res)

    def test_58(self):
        """首页-平台服务-纠纷调解"""
        nologinpage = NoLoginHomePage(self.homepage)
        nologinpage.get_url()
        nologinpage.tail_service_mediate()
        res = nologinpage.verification_mid_mediate()  # 验证方法为进入在线纠纷调解
        self.assertEqual(True, res)

    def test_59(self):
        """首页-平台服务-法律咨询"""
        nologinpage = NoLoginHomePage(self.homepage)
        nologinpage.get_url()
        nologinpage.tail_service_consult()
        res = nologinpage.verification_head_service_online_chat(
        )  # 验证方法为进入智能咨询页面
        self.assertEqual(True, res)

    def test_60(self):
        """首页-平台服务-在线评估"""
        nologinpage = NoLoginHomePage(self.homepage)
        nologinpage.get_url()
        nologinpage.tail_service_assess()
        res = nologinpage.verification_skip_login_page()  # 验证方法为跳转登陆页面
        self.assertEqual(True, res)

    def test_61(self):
        """首页-平台服务-在线仲裁"""
        nologinpage = NoLoginHomePage(self.homepage)
        nologinpage.get_url()
        nologinpage.tail_service_arbitration()
        nologinpage.change_windows()
        res = nologinpage.verification_arbitration()  # 验证方法为跳转在线仲裁URL
        self.assertEqual(True, res)

    def test_62(self):
        """首页-平台服务-诉讼服务"""
        nologinpage = NoLoginHomePage(self.homepage)
        nologinpage.get_url()
        nologinpage.tail_service_lawshit()
        nologinpage.change_windows()
        res = nologinpage.verification_lawshit()  # 验证方法为跳转诉讼服务URL
        self.assertEqual(True, res)

    def test_63(self):
        """首页-平台服务-反家暴服务"""
        nologinpage = NoLoginHomePage(self.homepage)
        nologinpage.get_url()
        nologinpage.tail_service_fjb()
        nologinpage.change_windows()
        res = nologinpage.verification_fjb_service_url()  # 验证方法为跳转反家暴服务URL
        self.assertEqual(True, res)

    def test_64(self):
        """首页-法律指南-婚姻继承"""
        nologinpage = NoLoginHomePage(self.homepage)
        nologinpage.get_url()
        nologinpage.tail_law_marriage()
        res = nologinpage.verification_tail_law_marriage()
        self.assertEqual(True, res)

    def test_65(self):
        """首页-法律指南-合同纠纷"""
        nologinpage = NoLoginHomePage(self.homepage)
        nologinpage.get_url()
        nologinpage.tail_law_argument()
        res = nologinpage.verification_tail_law_argument()
        self.assertEqual(True, res)

    def test_66(self):
        """首页-法律指南-交通事故"""
        nologinpage = NoLoginHomePage(self.homepage)
        nologinpage.get_url()
        nologinpage.tail_law_traffic()
        res = nologinpage.verification_tail_law_traffic()
        self.assertEqual(True, res)

    def test_67(self):
        """首页-法律指南-借贷纠纷"""
        nologinpage = NoLoginHomePage(self.homepage)
        nologinpage.get_url()
        nologinpage.tail_law_borrow()
        res = nologinpage.verification_tail_law_borrow()
        self.assertEqual(True, res)

    def test_68(self):
        """首页-关于我们-商务合作"""
        nologinpage = NoLoginHomePage(self.homepage)
        nologinpage.get_url()
        nologinpage.tail_ours_business()
        res = nologinpage.verification_tail_ours()
        self.assertEqual(True, res)

    def test_69(self):
        """首页-关于我们-联系方式"""
        nologinpage = NoLoginHomePage(self.homepage)
        nologinpage.get_url()
        nologinpage.tail_ours_contant()
        res = nologinpage.verification_tail_ours()
        self.assertEqual(True, res)

    def test_70(self):
        """首页-关于我们-服务条款"""
        nologinpage = NoLoginHomePage(self.homepage)
        nologinpage.get_url()
        nologinpage.tail_ours_service()
        res = nologinpage.verification_tail_ours()
        self.assertEqual(True, res)


if __name__ == '__main__':
    unittest.main()
