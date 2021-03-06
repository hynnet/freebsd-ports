# Created by: Wen Heping <wen@FreeBSD.org>
# $FreeBSD$

PORTNAME=	Moo
PORTVERSION=	1.007000
PORTREVISION=	1
CATEGORIES=	devel perl5
MASTER_SITES=	CPAN
MASTER_SITE_SUBDIR=	CPAN:HAARG
PKGNAMEPREFIX=	p5-

MAINTAINER=	perl@FreeBSD.org
COMMENT=	Minimalist Object Orientation (with Moose compatibility)

LICENSE=	ART10 GPLv1
LICENSE_COMB=	dual

BUILD_DEPENDS=	p5-Class-Method-Modifiers>=1.10:${PORTSDIR}/devel/p5-Class-Method-Modifiers \
		p5-Devel-GlobalDestruction>=0.11:${PORTSDIR}/devel/p5-Devel-GlobalDestruction \
		p5-Module-Runtime>=0.012:${PORTSDIR}/devel/p5-Module-Runtime \
		p5-Role-Tiny>=1.003.002:${PORTSDIR}/devel/p5-Role-Tiny \
		p5-strictures>=1.004003:${PORTSDIR}/devel/p5-strictures \
		p5-Import-Into>=1.002000:${PORTSDIR}/devel/p5-Import-Into
RUN_DEPENDS:=	${BUILD_DEPENDS}
TEST_DEPENDS=	p5-Test-Fatal>=0.003:${PORTSDIR}/devel/p5-Test-Fatal

USES=		perl5
USE_PERL5=	configure

OPTIONS_DEFINE=	XS
XS_DESC=	Use XS libraries for speed boost

XS_BUILD_DEPENDS=	p5-Class-XSAccessor>=1.18:${PORTSDIR}/devel/p5-Class-XSAccessor \
			p5-Sub-Name>=0:${PORTSDIR}/devel/p5-Sub-Name
XS_RUN_DEPENDS:=	${XS_BUILD_DEPENDS}

.include <bsd.port.mk>
