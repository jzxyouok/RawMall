# coding:utf8
import os
import django

os.environ['DJANGO_SETTINGS_MODULE'] = 'lawmall_05.settings'
django.setup()
from dbapi.models import Product, ProductDetail


def delete_product():
    Product.objects.all().delete()
    ProductDetail.objects.all().delete()


def add_product():
    p1 = Product.objects.create(id=1, name=u'体验型法律顾问', price=980, customer=u'适合于初创筹备团队和10人以下的微型创业团队使用。',
                                iconfont=u'xe635;', type=1,
                                introduction=u'【体验型法律顾问】精打细算 步步为营 | 砖家宝最精简的法律顾问，满足初创团队最基本的法律需求。')
    p1.productdetail_set.create(iconfont=u'xe600;', item=u'电话咨询全年无限次', desc=u'只需留下电话,律师10分钟快速响应')
    p1.productdetail_set.create(iconfont=u'xe705;', item=u'精品合同全年3次', desc=u'专享平台精品合同功能,10分钟快速响应,6小时内提交工作成果')
    p1.productdetail_set.create(iconfont=u'xe705;', item=u'精品合同全年3次', desc=u'专享平台精品合同功能,10分钟快速响应,6小时内提交工作成果')
    p1.productdetail_set.create(iconfont=u'xe605;', item=u'律师函全年1次', desc=u'律师为您撰写律师函,你可以把律师函邮寄给自己,也可以选择让律师代为邮寄')
    p1.productdetail_set.create(iconfont=u'xe6e9;', item=u'预约上门全年1次', desc=u'填写上门时间与上门地点,在线预约律师上门,最多可预约5天内的律师上门')
    p1.save()

    p1 = Product.objects.create(id=2, name=u'初创型法律顾问', price=2680, customer=u'适合于初创筹备团队和10人以下的微型创业团队使用。',
                                iconfont=u'xe63c;', type=1,
                                introduction=u'【初创型法律顾问】久经历练 始终经典 | 砖家宝经久不衰的人气产品，快速解决公司注册、初始过程中的法律问题。')
    p1.productdetail_set.create(iconfont=u'xe602;', item=u'快速咨询全年无限次', desc=u'专享平台快速咨询功能,10分钟快速响应')
    p1.productdetail_set.create(iconfont=u'xe600;', item=u'电话咨询全年无限次', desc=u'只需留下电话,律师10分钟快速响应')
    p1.productdetail_set.create(iconfont=u'xe705', item=u'精品合同全年5次', desc=u'专享平台精品合同功能,10分钟快速响应,6小时内提交工作成果')
    p1.productdetail_set.create(iconfont=u'xe605;', item=u'律师函全年1次', desc=u'律师为您撰写律师函,你可以把律师函邮寄给自己,也可以选择让律师代为邮寄')
    p1.productdetail_set.create(iconfont=u'xe6e9;', item=u'预约上门全年1次', desc=u'填写上门时间与上门地点,在线预约律师上门,最多可预约5天内的律师上门')
    p1.save()

    p1 = Product.objects.create(id=3, name=u'成长型法律顾问', price=4980, customer=u'适合于10-20人左右的小微型创业团队。', iconfont=u'xe638;',
                                type=1,
                                introduction=u'【成长型法律顾问】小微企业法律风险的天敌 | 一款以超低价格即可轻松获取的法律顾问，快乐创业之旅，怎能缺少安全相伴。')
    p1.productdetail_set.create(iconfont=u'xe602;', item=u'快速咨询全年无限次', desc=u'专享平台快速咨询功能,10分钟快速响应')
    p1.productdetail_set.create(iconfont=u'xe600;', item=u'电话咨询全年无限次', desc=u'只需留下电话,律师10分钟快速响应')
    p1.productdetail_set.create(iconfont=u'xe705;', item=u'精品合同全年10次', desc=u'专享平台精品合同功能,10分钟快速响应,6小时内提交工作成果')
    p1.productdetail_set.create(iconfont=u'xe605;', item=u'律师函全年2次', desc=u'律师为您撰写律师函,你可以把律师函邮寄给自己,也可以选择让律师代为邮寄')
    p1.productdetail_set.create(iconfont=u'xe6e9;', item=u'预约上门全年2次', desc=u'填写上门时间与上门地点,在线预约律师上门,最多可预约5天内的律师上门')
    p1.save()

    p1 = Product.objects.create(id=4, name=u'领先型法律顾问', price=9800, customer=u'适合于20-50人的小型创业团队。', iconfont=u'xe62e;',
                                type=1,
                                introduction=u'【领先型法律顾问】营造全企业安全新氛围 | 一款攻守兼备的法律顾问，日常法律风险一网打尽，让您轻松洞察先机。')
    p1.productdetail_set.create(iconfont=u'xe600;', item=u'快速咨询全年无限次', desc=u'专享平台快速咨询功能,10分钟快速响应')
    p1.productdetail_set.create(iconfont=u'xe602;', item=u'电话咨询全年无限次', desc=u'只需留下电话,律师10分钟快速响应')
    p1.productdetail_set.create(iconfont=u'xe705;', item=u'精品合同全年18次', desc=u'专享平台精品合同功能,10分钟快速响应,6小时内提交工作成果')
    p1.productdetail_set.create(iconfont=u'xe605;', item=u'律师函全年4次', desc=u'律师为您撰写律师函,你可以把律师函邮寄给自己,也可以选择让律师代为邮寄')
    p1.productdetail_set.create(iconfont=u'xe6e9;', item=u'预约上门全年3次', desc=u'填写上门时间与上门地点,在线预约律师上门,最多可预约5天内的律师上门')
    p1.save()

    p1 = Product.objects.create(id=5, name=u'旗舰型法律顾问', price=16800, customer=u'适合于30-80人的中型创业团队。', iconfont=u'xe621;',
                                type=1,
                                introduction=u'【旗舰型法律顾问】稳驭当下 方能致远  |  感受智尚豪华法律服务套装，尊享安稳商业之旅。')
    p1.productdetail_set.create(iconfont=u'xe600;', item=u'快速咨询全年无限次', desc=u'专享平台快速咨询功能,10分钟快速响应')
    p1.productdetail_set.create(iconfont=u'xe602;', item=u'电话咨询全年无限次', desc=u'只需留下电话,律师10分钟快速响应')
    p1.productdetail_set.create(iconfont=u'xe705;', item=u'精品合同全年30次', desc=u'专享平台精品合同功能,10分钟快速响应,6小时内提交工作成果')
    p1.productdetail_set.create(iconfont=u'xe605;', item=u'律师函全年8次', desc=u'律师为您撰写律师函,你可以把律师函邮寄给自己,也可以选择让律师代为邮寄')
    p1.productdetail_set.create(iconfont=u'xe6e9;', item=u'预约上门全年6次', desc=u'填写上门时间与上门地点,在线预约律师上门,最多可预约5天内的律师上门')
    p1.save()

    p1 = Product.objects.create(id=6, name=u'劳动用工专项法律顾问', price=1980, customer='', iconfont=u'xe62f;', type=2,
                                introduction=u'【劳动用工专项法律顾问】知人善任是企业发展的基础，我们由专业律师带头，为用户节约用工成本，规避劳动用工风险，全面解决员工离职的后顾之忧。')
    p1.productdetail_set.create(iconfont=u'xe63d;', item=u'劳动用工体系专项服务1次',
                                desc=u'全年免费法律咨询；\n根据企业具体需求定制员工规章制度；\n完善相关法律文件；提供1次争议和解谈判服务；\n争议标的额在10万以内的劳动仲裁/诉讼1次。')
    p1.save()

    p1 = Product.objects.create(id=7, name=u'股权架构专项法律顾问', price=4980, customer='', iconfont=u'xe62f;', type=2,
                                introduction=u'【股权架构专项法律顾问】从股权分配方案到持股比例设计，从股权份额预留到股东进退机制，我们将全程为您推荐业界资深的股权设计领域律师提供个性化服务。')
    p1.productdetail_set.create(iconfont=u'xe62c;', item=u'股权架构专项服务1次',
                                desc=u'全年免费法律咨询；\n根据企业具体需求定制股权架构设计方案及电子演示文稿；\n列席企业股东会议，充分讲解方案利弊；\n完善相关法律文件。')
    p1.save()

    p1 = Product.objects.create(id=8, name=u'员工激励专项法律顾问', price=16800, customer=u'', type=2,
                                iconfont=u'xe621;',
                                introduction=u'【员工激励专项法律顾问】要想成为当世伯乐，稳定团队信心，提高团队效率，凝聚核心人才。既要有容乃大的情怀，也离不开专业律师为公司设计科学精准的员工利益分配方案。')
    p1.productdetail_set.create(iconfont=u'xe62c;', item=u'股权架构专项服务1次',
                                desc=u'全年免费法律咨询；\n根据企业具体需求定制期权激励方案及电子演示文稿；\n列席企业决策层会议，充分讲解方案利弊；\n完善相关法律文件。')
    p1.save()


def main():
    delete_product()
    add_product()


# add_product()

if __name__ == '__main__':
    main()
