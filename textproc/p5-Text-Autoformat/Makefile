# Created by: Anton Berezin <tobez@tobez.org>
# $FreeBSD$

PORTNAME=	Text-Autoformat
PORTVERSION=	1.670.000
CATEGORIES=	textproc perl5
MASTER_SITES=	CPAN/../../authors/id/N/NE/NEILB
PKGNAMEPREFIX=	p5-
DISTNAME=	${PORTNAME}-${PORTVERSION:C/0\.(000)$//}

MAINTAINER=	tobez@FreeBSD.org
COMMENT=	Automatic and manual text wrapping and reformating formatting

BUILD_DEPENDS=	p5-version>=0:${PORTSDIR}/devel/p5-version \
		p5-Text-Reform>=1.11:${PORTSDIR}/textproc/p5-Text-Reform
RUN_DEPENDS:=	${BUILD_DEPENDS}

USES=		perl5
USE_PERL5=	configure

.include <bsd.port.mk>
