# Created by: Adam Weinberger <adamw@FreeBSD.org>
# $FreeBSD$

PORTNAME=	Mojo-Pg
PORTVERSION=	1.10
CATEGORIES=	databases www perl5
MASTER_SITES=	CPAN
MASTER_SITE_SUBDIR=	CPAN:SRI
PKGNAMEPREFIX=	p5-

MAINTAINER=	perl@FreeBSD.org
COMMENT=	PostgreSQL integration for p5-Mojolicious

LICENSE=	ART20

BUILD_DEPENDS=	p5-Mojolicious>=5.81:${PORTSDIR}/www/p5-Mojolicious \
		p5-DBD-Pg>=0:${PORTSDIR}/databases/p5-DBD-Pg
RUN_DEPENDS:=	${BUILD_DEPENDS}

USES=		perl5
USE_PERL5=	configure

.include <bsd.port.mk>
