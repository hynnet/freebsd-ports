# Created by: Kurt Lidl <kurt.lidl@cello.com>
# $FreeBSD$

PORTNAME=	Data-Rx
PORTVERSION=	0.200006
PORTREVISION=	1
CATEGORIES=	devel perl5
MASTER_SITES=	CPAN
PKGNAMEPREFIX=	p5-

MAINTAINER=	perl@FreeBSD.org
COMMENT=	Perl implementation of Rx schema system

LICENSE=	ART10 GPLv1
LICENSE_COMB=	dual

BUILD_DEPENDS=	p5-File-Find-Rule>=0:${PORTSDIR}/devel/p5-File-Find-Rule \
		p5-JSON>=2:${PORTSDIR}/converters/p5-JSON \
		p5-Number-Tolerant>=0:${PORTSDIR}/devel/p5-Number-Tolerant
RUN_DEPENDS:=	${BUILD_DEPENDS}
TEST_DEPENDS=	p5-Sub-Exporter>=0:${PORTSDIR}/devel/p5-Sub-Exporter \
		p5-Test-Deep>=0:${PORTSDIR}/devel/p5-Test-Deep \
		p5-Try-Tiny>=0:${PORTSDIR}/lang/p5-Try-Tiny

USES=		perl5
USE_PERL5=	configure

.include <bsd.port.mk>
